from pydantic import BaseModel


class AnalyticsRequest(BaseModel):
    market: str
    currency: str
