# SafeSwapGlobal MCP Server

[![Smithery](https://smithery.ai/badge/safeswapglobal/crypto-quote)](https://smithery.ai/servers/safeswapglobal/crypto-quote)
[![SafeSwapGlobal Crypto Swap Quotes MCP connector – tool definition quality and endpoint health on Glama](https://glama.ai/mcp/connectors/online.safeswapglobal.rates/safe-swap-global-crypto-swap-quotes/badges/score.svg)](https://glama.ai/mcp/connectors/online.safeswapglobal.rates/safe-swap-global-crypto-swap-quotes)

Official Model Context Protocol (MCP) server for [SafeSwapGlobal](https://safeswapglobal.online) — an independent, non-custodial cryptocurrency swap directory.

Allows AI agents, developers, and LLM applications to retrieve real-time cross-chain liquidity quotes, limits, and non-custodial execution URLs.

## Features
- **Real-Time Rates:** Powered by live on-chain liquidity depth across 240+ corridors.
- **Zero Custody:** Direct wallet-to-wallet execution parameters.
- **No API Keys Required:** Free public infrastructure for Web3 developers and autonomous agents.

## Public Endpoints
- **Remote MCP Endpoint:** `https://rates.safeswapglobal.online`
- **REST JSON Quote:** `GET https://rates.safeswapglobal.online/quote?from=BTC&to=XMR&amount=1`

## 🛠 Available Tools
- `get_swap_quote`: Real-time cross-chain floating rates, fees, limits, and execution parameters (240+ pairs).
- `list_supported_currencies`: Complete catalog of 15 supported blockchains and assets.

## 🚀 Quickstart: Connect to AI Clients

### 1. Claude Desktop
Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "safeswapglobal": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://rates.safeswapglobal.online"
      ]
    }
  }
}
```

### 2. Cursor / Windsurf
Add a new MCP server in settings:
- **Type:** SSE / Streamable HTTP
- **URL:** `https://rates.safeswapglobal.online`

## 🤖 For AI Agents
See [AGENTS.md](./AGENTS.md) for full Model Context Protocol specifications, Cursor/Windsurf rules, and architectural guidelines.

## License
Released under the [MIT License](LICENSE).
