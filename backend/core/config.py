from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables.

    Values can be overridden via a `.env` file placed in the backend root.
    """

    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    model_name: str = Field(default="gpt-5-nano", alias="MODEL_NAME")
    temperature: float = Field(default=0.2, alias="TEMPERATURE")
    max_tokens: int = Field(default=1500, alias="MAX_TOKENS")

    upload_max_mb: int = Field(default=10, alias="UPLOAD_MAX_MB")
    allowed_origins: str = Field(default="*", alias="ALLOWED_ORIGINS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


