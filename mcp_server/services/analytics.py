from typing import Any

from ..client import ApiClient


class AnalyticsService:
    """Service layer for analytics endpoints."""

    def __init__(self, client: ApiClient) -> None:
        self.client = client

    async def atm_implied_volatility_ts(self, market: str, currency: str) -> Any:
        endpoint = f"/analytics/options/atm_iv_ts/{market}/{currency}"
        return await self.client.get(endpoint)
