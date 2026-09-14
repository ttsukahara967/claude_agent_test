# Claude Agent SDK Sample

A minimal sample project for the Claude Agent SDK (Python). It defines a
custom calculator tool and has Claude use it to perform a calculation.

## Getting an API Key

1. Go to [console.anthropic.com](https://console.anthropic.com) and sign in (or create an account).
2. Open **API Keys** in the left sidebar (under Settings).
3. Click **Create Key** and copy the generated key — it's only shown once.
4. Add credit to your account under **Billing** if you haven't already (usage is billed pay-as-you-go).

## Setup

```bash
/opt/homebrew/bin/python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `ANTHROPIC_API_KEY` to the key you created above.

```bash
cp .env.example .env
```

## Run

```bash
source .venv/bin/activate
python agent.py
```

## What's inside

- `agent.py`: registers two custom tools, `add` and `multiply`, as an SDK MCP
  server, then calls `query()` to have Claude use them to solve a calculation.
  It also prints the API cost and token usage for each run.
