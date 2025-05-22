from mcp.server.fastmcp import FastMCP

from ..client import ApiClient
from ..services.analytics import AnalyticsService
from ..schemas.analytics import AnalyticsRequest


class AnalyticsController:
    def __init__(self, mcp: FastMCP, client: ApiClient) -> None:
        self.service = AnalyticsService(client)
        self._register_tools(mcp)

    def _register_tools(self, mcp: FastMCP) -> None:
        @mcp.tool()
        async def get_atm_implied_volatility_timelapse(market: str, currency: str) -> dict:
            req = AnalyticsRequest(market=market, currency=currency)
            return await self.service.atm_implied_volatility_ts(req.market, req.currency)
