from typing import Any, Dict, Optional

import httpx

from .config import get_settings


class ApiClient:
    """Wrapper around httpx.AsyncClient with predefined settings."""

    def __init__(self) -> None:
        self.settings = get_settings()
        self._client = httpx.AsyncClient(
            base_url=self.settings.base_url,
            headers={"apiKey": self.settings.api_key},
            timeout=self.settings.timeout,
        )

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        response = await self._client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    async def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        response = await self._client.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()

    async def __aenter__(self) -> "ApiClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._client.__aexit__(exc_type, exc, tb)
