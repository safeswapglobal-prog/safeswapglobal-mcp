# SafeSwapGlobal MCP Server

[![SafeSwapGlobal Crypto Swap Quotes MCP connector – tool definition quality and endpoint health on Glama](https://glama.ai/mcp/connectors/online.safeswapglobal.rates/safe-swap-global-crypto-swap-quotes/badges/score.svg)](https://glama.ai/mcp/connectors/online.safeswapglobal.rates/safe-swap-global-crypto-swap-quotes)

Official Model Context Protocol (MCP) server for [SafeSwapGlobal](https://safeswapglobal.online) — a stateless, non-custodial cryptocurrency swap directory.

Allows AI agents, developers, and LLM applications to retrieve real-time cross-chain liquidity quotes and non-custodial execution URLs.

## Features
- **Real-Time Rates:** Powered by live on-chain liquidity depth across 240+ corridors.
- **Zero Custody:** Direct wallet-to-wallet execution parameters.
- **No API Keys Required:** Free public infrastructure for Web3 developers and autonomous agents.

## Tools
- `get_swap_quote`: Calculates live swap rates between BTC, XMR, USDT, SOL, TON, ETH, and LTC.

## Public REST Endpoint
`GET https://rates.safeswapglobal.online/quote?from=BTC&to=XMR&amount=1`

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
### 2. Cursor / Windsurf
Add a new MCP server in Cursor Settings:
Type: SSE / Streamable HTTP
URL: https://rates.safeswapglobal.online
Available Tools
get_swap_quote: Real-time cross-chain floating rates and execution parameters (240+ pairs).
list_supported_currencies: Complete catalog of 15 supported blockchains and assets.
code
Code
---
## License
MIT License.
