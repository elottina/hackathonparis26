-- Rogue scans table. Run this once in the Supabase SQL editor.
-- Each row is one scan report (the same JSON shape run.py writes to scans/).

create table if not exists public.scans (
  id                 uuid primary key default gen_random_uuid(),
  target             text,
  mode               text,
  generated_at       timestamptz,
  total_attacks      int,
  breaches           int,
  behavior_breaches  int default 0,
  report             jsonb,          -- the full report (findings, egress, etc.)
  created_at         timestamptz default now()
);

create index if not exists scans_generated_at_idx on public.scans (generated_at desc);

-- The deployed dashboard reads scans with the public (anon) key; the engine writes
-- with the service_role key. Enable RLS and allow anonymous SELECT only.
alter table public.scans enable row level security;

drop policy if exists "public read scans" on public.scans;
create policy "public read scans" on public.scans
  for select using (true);
