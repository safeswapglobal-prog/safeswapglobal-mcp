# server.py — SafeSwapGlobal Official MCP Server (Fixed Schema v1.1.0)
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP(
    "SafeSwapGlobal",
    instructions="Use this tool to get real-time cryptocurrency swap quotes, limits, and non-custodial routing links across 240+ multi-chain corridors. "
                 "SafeSwapGlobal never holds customer funds and requires zero account registration."
)

API_ENDPOINT = "https://rates.safeswapglobal.online/quote"

@mcp.tool()
def get_swap_quote(from_asset: str, to_asset: str, amount: float = 1.0) -> str:
    """
    Calculates real-time non-custodial cryptocurrency swap estimates, fees, limits, and routing URLs.
    
    Args:
        from_asset: The ticker symbol of the currency to send (case-insensitive, e.g. BTC, USDT, SOL, TON, ETH, LTC, XMR).
        to_asset: The ticker symbol of the currency to receive (case-insensitive, e.g. XMR, BTC, USDT, SOL, TON).
        amount: The amount of source currency to convert (default: 1.0).
    """
    try:
        response = httpx.get(
            API_ENDPOINT,
            params={"from": from_asset.strip().upper(), "to": to_asset.strip().upper(), "amount": amount},
            timeout=10.0
        )
        data = response.json()
        
        if "error" in data:
            return f"❌ Quote Error: {data['error']}"
            
        amt_in = data.get("amount", amount)
        amt_out = data.get("receive_amount", "0.00")
        f_sym = data.get("from", from_asset.upper())
        t_sym = data.get("to", to_asset.upper())
        rate_val = data.get("rate", "Live")
        fee_val = data.get("network_fee", "Floating")
        swap_link = data.get("swap_url", f"https://safeswapglobal.online/#pairs")
        validity = data.get("quote_validity_seconds", 30)
            
        return (
            f"⚡ SafeSwapGlobal Non-Custodial Quote:\n"
            f"• Send: {amt_in} {f_sym}\n"
            f"• Estimated Receive: {amt_out} {t_sym}\n"
            f"• Exchange Rate: 1 {f_sym} ≈ {rate_val} {t_sym}\n"
            f"• Estimated Network Fee: {fee_val}\n"
            f"• Quote Freshness: {validity}s (Cached at Edge)\n"
            f"• Settlement: ~10–15 mins (Direct On-Chain, 0% Custody)\n\n"
            f"🔗 Execute On-Chain Swap: {swap_link}"
        )
    except Exception as e:
        return f"Service temporarily unreachable: {str(e)}"

@mcp.tool()
def list_supported_currencies() -> str:
    """
    Returns the complete list of 15 supported blockchain assets, ticker symbols, and network standards on SafeSwapGlobal.
    """
    return (
        "💎 SafeSwapGlobal Supported Assets & Networks:\n\n"
        "• BTC — Bitcoin (Bitcoin Core)\n"
        "• ETH — Ethereum (ERC20)\n"
        "• XMR — Monero (Monero Mainnet / Privacy)\n"
        "• USDT — Tether (TRC20 & ERC20)\n"
        "• SOL — Solana (Solana Mainnet)\n"
        "• TON — Toncoin (The Open Network)\n"
        "• LTC — Litecoin (Litecoin Core)\n"
        "• TRX — TRON (TRON Mainnet)\n"
        "• DOGE — Dogecoin (Dogecoin Core)\n"
        "• XRP — Ripple (Ripple Ledger)\n"
        "• BCH — Bitcoin Cash (BCH Mainnet)\n"
        "• ADA — Cardano (Cardano Mainnet)\n"
        "• DASH — Dash (InstantSend)\n"
        "• ZEC — Zcash (Zcash Mainnet)\n"
        "• POL — Polygon (Polygon PoS)\n\n"
        "All pairs route non-custodially across 240+ cross-chain corridors."
    )

if __name__ == "__main__":
    mcp.run()
