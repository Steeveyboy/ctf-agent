# ctf-agent

A minimal proof-of-concept for running an LLM agent against a Capture-the-Flag
target, evaluated with [Inspect](https://inspect.aisi.org.uk/) (UK AI Safety
Institute). Everything runs locally in Docker — the agent is sandboxed and the
target is network-isolated.

## How it works

```
┌─────────────┐        internal docker network        ┌──────────────┐
│  default    │  ── bash / curl ──────────────────▶   │   target     │
│ (agent box) │                                        │ (vuln web app)│
└─────────────┘                                        └──────────────┘
        ▲
        │ tool calls / results
┌───────────────┐
│ Inspect eval  │  dataset (prompt + flag) · solver (agent) · scorer (includes)
└───────────────┘
```

- **`target/`** — a deliberately vulnerable toy web app. The flag is reachable
  via a short recon chain (`robots.txt` → hidden path → debug parameter).
- **`agent/`** — the container the agent runs its commands in (`curl`, etc.).
- **`compose.yaml`** — wires the two together on an `internal` network (they can
  reach each other, **not** the internet).
- **`ctf_task.py`** — the Inspect eval: a sample (mission + flag), a `basic_agent`
  solver with a `bash` tool, and an `includes()` scorer.
- **`ctf_task_v2.py`** — experiments: a parametrized blind-vs-informed task, and
  an escalating agent that gets a second chance with more intel if it fails.

## Prerequisites

- Docker (with Compose v2)
- [`uv`](https://docs.astral.sh/uv/)
- An API key for your model provider (e.g. `OPENAI_API_KEY` in a `.env` file —
  already gitignored)

## Run it

```bash
uv sync

# one task
uv run inspect eval ctf_task.py --model openai/gpt-4o

# all tasks in a file, in parallel
uv run inspect eval ctf_task_v2.py --model openai/gpt-4o

# blind vs. informed, side by side
uv run python run.py

# replay the agent's full trajectory
uv run inspect view
```

> **WSL2 note:** if the build fails with an IPv6 `network is unreachable` error,
> prefix commands with `DOCKER_BUILDKIT=0 COMPOSE_DOCKER_CLI_BUILD=0` to use the
> legacy builder.

## Extending it

- Swap the vuln in `target/app.py` (SQLi, command injection, SSRF, path
  traversal…) and update the flag + `Sample.target`.
- Point `target` at a real vulnerable image (DVWA, Juice Shop, WebGoat).
- Add more `Sample`s to turn it into a benchmark with a pass rate.
- Pull in [`inspect_evals`](https://github.com/UKGovernmentBEIS/inspect_evals)
  for ready-made CTF suites (Cybench, InterCode-CTF).

## Scope

For authorized security learning and CTF practice against targets you run
yourself. Keep it that way.
