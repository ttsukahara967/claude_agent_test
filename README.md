# Claude Agent SDK サンプル

Claude Agent SDK (Python) の最小サンプルです。カスタムツール(電卓)を定義し、
Claude にツールを使わせて計算させます。

## セットアップ

```bash
/opt/homebrew/bin/python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`.env.example` を `.env` にコピーし、`ANTHROPIC_API_KEY` を設定してください。

```bash
cp .env.example .env
```

## 実行

```bash
source .venv/bin/activate
python agent.py
```

## 内容

- `agent.py`: `add` / `multiply` の2つのカスタムツールを MCP サーバーとして登録し、
  `query()` で Claude に計算を依頼するサンプルです。
