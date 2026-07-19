# infra/firecrawl

**A recipe, not a running service.** These files are text: a compose file, an `.env.example`, and the searxng and postgres configs it needs. Nothing here starts unless you run `scripts/install-firecrawl`.

## If you already have a Firecrawl, this directory does nothing

`scripts/install-firecrawl` checks first, and stops if one is already answering. That check exists because standing up a second stack would actively hurt: the compose uses `network_mode: host`, so a second Firecrawl fights the first for ports 3002, 5432, 5672 and 6379, and both end up broken.

Point the tool at the one you have — `scripts/setup` asks for the URL.

## If you don't

`scripts/install-firecrawl` brings up six containers (api, playwright, redis, rabbitmq, postgres, searxng) from the published `ghcr.io/firecrawl/*` images, generates every secret, and — the part that matters — verifies that `/v2/search` **returns results**, not merely that `/` returns 200. Liveness only proves the process started. Search is what deep research actually depends on, and it is what silently breaks when searxng is misconfigured.

The alternative is the hosted API at [firecrawl.dev](https://firecrawl.dev), which needs no containers and has a free tier. `scripts/setup` offers both.

## Why the compose, rather than pointing at upstream's

Firecrawl's own self-host path is `git clone && docker compose build`, which compiles the whole thing. This runs the published images directly: same service, minutes faster, and nothing to keep in sync with upstream's tree.

## The failure worth knowing about

`MAX_CPU` and `MAX_RAM` in the `.env` are not advisory. Above those thresholds Firecrawl starts refusing connections (`Can't accept connection due to RAM/CPU load`) and eventually **shuts itself down cleanly — exit 0**, while the five support containers stay up and `docker compose ps` reads perfectly healthy. That is how a Firecrawl can be dead for days without anyone noticing.

`restart: unless-stopped` turns that silent disappearance into a recovery. If research runs start dying mid-way on a busy machine, raise those two numbers first.
