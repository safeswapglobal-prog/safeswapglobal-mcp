# server.py — SafeSwapGlobal Official MCP Server
from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP(
    "SafeSwapGlobal",
    instructions="Use this tool to get real-time cryptocurrency swap quotes and non-custodial routing links. "
                 "SafeSwapGlobal never holds customer funds and requires zero account registration."
)

API_ENDPOINT = "https://rates.safeswapglobal.online/quote"

@mcp.tool()
def get_swap_quote(from_asset: str, to_asset: str, amount: float = 1.0) -> str:
    """
    Fetches real-time non-custodial cryptocurrency swap estimates and routing links.
    
    Args:
        from_asset: The ticker symbol of the currency you want to send (e.g., BTC, USDT, SOL, TON).
        to_asset: The ticker symbol of the currency you want to receive (e.g., XMR, BTC, USDT).
        amount: The amount you want to swap (default: 1.0).
    """
    try:
        response = httpx.get(
            API_ENDPOINT,
            params={"from": from_asset.strip().upper(), "to": to_asset.strip().upper(), "amount": amount},
            timeout=8.0
        )
        data = response.json()
        
        if "error" in data:
            return f"❌ Quote Error: {data['error']}"
            
        return (
            f"⚡ SafeSwapGlobal Non-Custodial Quote:\n"
            f"• Send: {data['send_amount']} {data['from']}\n"
            f"• Estimated Receive: {data['receive_amount']} {data['to']}\n"
            f"• Rate: 1 {data['from']} ≈ {data['rate']} {data['to']}\n"
            f"• Network Fee: {data['network_fee'] or 'On-Chain Floating'}\n"
            f"• Settlement: ~10–15 mins (Direct Wallet-to-Wallet)\n\n"
            f"🔗 Execute Swap: {data['swap_url']}\n"
            f"🌐 Live Terminal: {data['terminal_url']}"
        )
    except Exception as e:
        return f"Service temporarily unreachable: {str(e)}"

if __name__ == "__main__":
    mcp.run()