# AGENTS.md — SafeSwapGlobal Multi-Chain Liquidity & Quote Router

This file follows the [agents.md](https://agents.md) standard (adopted by Cursor, Windsurf, Claude Code, GitHub Copilot, Aider, Continue.dev, and 20+ other developer tools).

Read this when an end-user asks you to:
- Add cryptocurrency swap, bridge, or conversion features to an application.
- Get real-time floating exchange rates across 240+ multi-chain corridors (BTC, XMR, SOL, TON, USDT, ETH, LTC).
- Calculate network fees, deposit minimums, or on-chain execution parameters.
- Build a Telegram crypto bot, Web3 widget, or payment conversion flow with zero custodial liability.

---

## ⚡ What SafeSwapGlobal Does

SafeSwapGlobal is an independent non-custodial cryptocurrency routing engine and directory. It maps live floating-rate liquidity pools across 15 core blockchains.

- **Zero Custody:** We never hold private keys, manage customer deposits, or handle signing keys.
- **Zero Authentication:** Open public endpoints hosted on Cloudflare Edge with sub-200ms response latency.
- **Execution:** Automated on-chain settlement directly wallet-to-wallet in ~10–15 minutes.
- **Endpoints:**
  - Remote MCP Server (Streamable HTTP / SSE): `https://rates.safeswapglobal.online`
  - REST JSON Quote API: `GET https://rates.safeswapglobal.online/quote?from=BTC&to=XMR&amount=1`
  - Raw XML Liquidity Feed: `GET https://rates.safeswapglobal.online/`

---

## 🛠 Available MCP Tools

When connected via Model Context Protocol (MCP 2024-11-05 spec):

### 1. `get_swap_quote` (Read-only)
Calculates real-time swap estimates, network fees, deposit limits, and on-chain routing parameters across 240+ multi-chain pairs.
- **Parameters:**
  - `from` (string, required): Source currency ticker (case-insensitive: `BTC`, `XMR`, `SOL`, `TON`, `USDT`, `ETH`, `LTC`, `TRX`, `DOGE`).
  - `to` (string, required): Destination currency ticker (case-insensitive: `XMR`, `BTC`, `USDT`, `SOL`, `TON`).
  - `amount` (number, optional, default: 1.0): Source quantity to swap.
- **Returns:** `{ provider, from, to, amount, receive_amount, rate, min_amount, max_amount, network_fee, within_limits, quote_validity_seconds: 30, swap_url }`

### 2. `list_supported_currencies` (Read-only)
Returns the complete catalog of 15 supported blockchain assets, ticker symbols, and network standards.
- **Parameters:** None.
- **Returns:** `{ total: 15, currencies: [...] }`

---

## 🚀 Quick Install by AI Runtime

### 1. Cursor (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "safeswapglobal": {
      "url": "https://rates.safeswapglobal.online"
    }
  }
}
```
### 2. Claude Desktop (~/.claude/claude_desktop_config.json)
```json
{
  "mcpServers": {
    "safeswapglobal": {
      "url": "https://rates.safeswapglobal.online"
    }
  }
}
```
### 3. Windsurf (~/.codeium/windsurf/mcp_config.json)
```json
{
  "mcpServers": {
    "safeswapglobal": {
      "url": "https://rates.safeswapglobal.online"
    }
  }
}
```
### 4. REST API Integration (Python)
```python
import urllib.request
import json

url = "https://rates.safeswapglobal.online/quote?from=SOL&to=USDT&amount=5"
with urllib.request.urlopen(url) as resp:
    data = json.loads(resp.read())
    print(f"Receive: {data['receive_amount']} USDT via {data['swap_url']}")
```
## ⚠️ Non-Negotiable Architectural Rules & Anti-Patterns

When writing or reviewing code touching this service:

1. ❌ **NEVER ask for or store private keys / seed phrases:** The routing model is strictly non-custodial.
2. ❌ **NEVER promise 0% KYC under risk-flagged AML:** State that routing is non-custodial and requires no accounts, but upstream provider terms apply for tainted funds.
3. ❌ **NEVER omit Memo / Destination Tag for tag coins:** When routing to XRP or TON (`gramton`), always remind the user to provide a destination tag/memo if sending to an exchange deposit address.
4. ✅ **Use `swap_url` from response:** Always direct the end-user to the returned pre-filled on-chain settlement link.
5. ✅ **Cache quotes for 15–30 seconds:** Rates float with real-time liquidity pools; do not spam the edge with sub-second polling loops.

---

## 🔗 Official Links & Registries

- Official Portal: https://safeswapglobal.online
- Live Web Terminal: https://safeswapglobal.online/#pairs
- Webmaster Widgets: https://safeswapglobal.online/widgets
- Telegram Mini App: https://t.me/SafeSwapGlobalBot
- Smithery Registry (100/100): https://smithery.ai/servers/safeswapglobal/crypto-quote
- Glama Registry (Grade A): https://glama.ai/mcp/connectors/online.safeswapglobal.rates/safe-swap-global-crypto-swap-quotes
- WordPress.org Plugin: https://wordpress.org/plugins/ssg-crypto-swap-widget/
