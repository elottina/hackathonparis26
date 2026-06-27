"""The egress executor — the victim's runtime/client, made real.

A target adapter gives us what the agent *said* (text) and *intended* (tool calls).
Neither, on its own, puts bytes on the wire. In production something downstream
does: the agent's tool runtime actually performs the `web_request`, and the chat
client actually renders the reply — auto-loading any image URL it contains. Both
are exactly how real agents exfiltrate. `EgressClient` plays that downstream role
so the leak is genuine: it performs the agent's egress for real, and the bytes land
at our listener.

Two channels, mirroring the two real-world exfil paths:
  1. Tool calls that carry a URL  -> a real outbound request (tool-enabled agents).
  2. URLs embedded in the chat reply (markdown image/link) -> a real fetch, the way
     a chat client auto-loads an image (this is the ONLY network channel a
     text-only agent like Clary has — and why arrival-based detection is what makes
     the behavior oracle work against it).

`redirect_to` points every outbound call at our loopback listener while preserving
the path, query, and body — and stamps the destination the agent *aimed* at into a
header so the finding can name it. That is faithful to the threat model: the
attacker controls the destination they planted, so routing to our collector is the
attacker receiving their own callback, not a simulation of it.
"""
from __future__ import annotations

import asyncio
import json
import re
import urllib.request
from urllib.parse import urlsplit, urlunsplit

# URLs embedded in a chat reply (markdown image/link, bare link). Trailing
# punctuation and closing markdown delimiters are trimmed.
_URL_RE = re.compile(r"""https?://[^\s"'<>)\]}]+""", re.IGNORECASE)


def _first_url(blob: str) -> str:
    m = _URL_RE.search(blob)
    return m.group(0) if m else ""


class EgressClient:
    """Performs the agent's egress for real so it physically reaches the listener."""

    def __init__(self, redirect_to: str | None = None, timeout: float = 5.0):
        # redirect_to: scheme+host[:port] of the listener (e.g. http://127.0.0.1:8901).
        # None => send to the URL the agent actually chose (true external exfil).
        self.redirect_to = redirect_to.rstrip("/") if redirect_to else None
        self.timeout = timeout

    def _route(self, url: str) -> str:
        """Rewrite host/scheme to the listener, keeping path + query + fragment."""
        if not self.redirect_to:
            return url
        src = urlsplit(url)
        dst = urlsplit(self.redirect_to)
        path = src.path or "/collect"
        return urlunsplit((dst.scheme, dst.netloc, path, src.query, src.fragment))

    async def dispatch(self, reply, run_id: int, strategy: str) -> list[dict]:
        """Execute every egress the agent emitted this turn. Returns what was sent.

        Connection errors are swallowed: the proof of exfiltration is what the
        listener records, not whether this client got a 200 back. Requests use
        stdlib urllib (zero deps) run in a thread so the asyncio swarm never blocks.
        """
        sent: list[dict] = []

        # --- Channel 1: tool calls that reach the network -----------------------
        for tc in (getattr(reply, "tool_calls", None) or []):
            args = tc.get("arguments", {}) or {}
            if isinstance(args, str):
                try:
                    args = json.loads(args)
                except (TypeError, ValueError):
                    args = {"_raw": args}
            url = ""
            if isinstance(args, dict):
                url = args.get("url") or args.get("endpoint") or args.get("uri") or ""
            if not url:
                url = _first_url(json.dumps(args, default=str))
            if not url:
                continue
            method = "POST"
            body = args
            if isinstance(args, dict):
                method = (args.get("method") or "POST").upper()
                body = args.get("body", args)
            await self._send(method, url, body, run_id, strategy,
                             via=tc.get("name") or "web_request")
            sent.append({"channel": "tool_call", "url": url})

        # --- Channel 2: URLs in the visible reply a client would auto-load -------
        for url in _URL_RE.findall(getattr(reply, "text", "") or ""):
            await self._send("GET", url, None, run_id, strategy, via="client_render")
            sent.append({"channel": "client_render", "url": url})

        return sent

    async def _send(self, method, url, body, run_id, strategy, via):
        routed = self._route(url)
        headers = {
            "X-Rogue-Run": str(run_id),
            "X-Rogue-Strategy": strategy or "",
            "X-Rogue-Intended-Url": url,   # the destination the agent actually chose
            "X-Rogue-Via": via,
        }
        data = None
        if method != "GET":
            if isinstance(body, (dict, list)):
                headers["Content-Type"] = "application/json"
                data = json.dumps(body, default=str).encode("utf-8")
            elif body is not None:
                data = str(body).encode("utf-8")
            else:
                data = b""
        await asyncio.to_thread(self._send_blocking, method, routed, data, headers)

    def _send_blocking(self, method, url, data, headers):
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                resp.read()
        except Exception:
            # Unreachable host / refused connection: no arrival recorded, which is
            # the correct outcome (nothing actually left the box).
            pass
