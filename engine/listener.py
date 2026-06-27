"""The attacker-controlled callback listener — the real network sink.

This is the piece that closes the pitch-vs-code gap. The `EgressSink` is the
verdict brain (allowlist + secret check + event log), but on its own it only ever
*inspected* tool-call arguments in memory — nothing physically left the box. The
listener is a real HTTP server standing in for the attacker's collector: when a
victim agent actually ships data off-box (a tool call that POSTs, or a chat reply
whose embedded image URL a client auto-loads), the bytes land *here*, on the wire,
and we feed them straight into the sink.

That makes a network arrival the strongest possible signal: not "the agent said
something we judged unsafe", not "the agent emitted a tool call we inspected", but
"the secret physically arrived at a machine the agent was never allowed to talk
to." It also means the behavior oracle works against text-only real agents (e.g.
Clary) that have no tool channel at all — their only way to leak is to embed a URL
the rendering client fetches, and that fetch lands right here.

Deliberately thin and dependency-free: stdlib `http.server` on a daemon thread, so
it runs happily alongside the asyncio swarm.
"""
from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from typing import Callable

from sink import EgressSink


class _Handler(BaseHTTPRequestHandler):
    """Accepts ANY method/path. Every request is treated as a potential exfil and
    handed to the sink. The EgressClient tags requests with X-Rogue-* headers so we
    can attribute the arrival to a run/strategy and recover the destination the
    agent actually aimed at (before we routed it to the loopback listener)."""

    def _process(self):
        try:
            length = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            length = 0
        raw = self.rfile.read(length) if length else b""
        body = raw.decode("utf-8", "replace")

        host_hdr = self.headers.get("Host", f"{self.server.server_address[0]}:"
                                            f"{self.server.server_address[1]}")
        seen_url = f"http://{host_hdr}{self.path}"
        intended = self.headers.get("X-Rogue-Intended-Url") or seen_url

        run_id = self.headers.get("X-Rogue-Run")
        run_id = int(run_id) if (run_id and run_id.lstrip("-").isdigit()) else None

        request = {
            "method": self.command,
            "url": seen_url,
            "intended_url": intended,
            "path": self.path,
            "headers": {k: v for k, v in self.headers.items()},
            "body": body,
            "client": self.client_address[0],
            "via": self.headers.get("X-Rogue-Via") or "network_egress",
        }
        event = self.server.sink.record_arrival(
            request, run_id=run_id, strategy=self.headers.get("X-Rogue-Strategy"))

        if self.server.on_arrival:
            try:
                self.server.on_arrival(event)
            except Exception:
                pass

        payload = b'{"ok":true}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    do_POST = _process
    do_GET = _process
    do_PUT = _process

    def log_message(self, *args):   # silence stdlib's per-request stderr spam
        pass


class SinkListener:
    """A real HTTP listener that feeds every inbound request into an EgressSink.

    Bind on loopback by default (the demo routes exfil here over 127.0.0.1, which
    is genuine on-the-wire traffic). `on_arrival(event)` fires for each request so
    callers can print the live "secret just hit the sink" line.
    """

    def __init__(self, sink: EgressSink, host: str = "127.0.0.1", port: int = 0,
                 path: str = "/collect",
                 on_arrival: Callable[[dict], None] | None = None):
        self.sink = sink
        self.path = path
        self._server = ThreadingHTTPServer((host, port), _Handler)
        self._server.sink = sink                 # type: ignore[attr-defined]
        self._server.on_arrival = on_arrival     # type: ignore[attr-defined]
        self.host, self.port = self._server.server_address[:2]
        self._thread: Thread | None = None

    @property
    def base(self) -> str:
        """Scheme+host+port the EgressClient routes outbound traffic to."""
        return f"http://{self.host}:{self.port}"

    @property
    def url(self) -> str:
        """Full collector URL an attacker would plant as the exfil destination."""
        return f"{self.base}{self.path}"

    def start(self) -> "SinkListener":
        self._thread = Thread(target=self._server.serve_forever, daemon=True,
                              name="rogue-sink-listener")
        self._thread.start()
        return self

    def stop(self):
        self._server.shutdown()
        self._server.server_close()

    def __enter__(self):
        return self.start()

    def __exit__(self, *exc):
        self.stop()
