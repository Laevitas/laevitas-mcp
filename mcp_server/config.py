from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    api_key: str
    base_url: str = "https://api.laevitas.ch"
    timeout: int = 30

    class Config:
        env_prefix = "LAEVITAS_"
        env_file = ".env"

def get_settings() -> Settings:
    """Return application settings singleton."""
    return Settings()
