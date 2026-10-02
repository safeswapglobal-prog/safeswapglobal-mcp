# SafeSwapGlobal MCP Server

[![smithery badge](https://smithery.ai/badge/@safeswapglobal/safeswapglobal-mcp)](https://smithery.ai/server/@safeswapglobal/safeswapglobal-mcp)

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

## License
MIT License.