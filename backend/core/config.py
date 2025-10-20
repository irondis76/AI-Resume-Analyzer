from __future__ import annotations

import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration loaded from environment variables.

    Values can be overridden via a `.env` file placed in the backend root.
    """

    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    model_name: str = Field(default="gpt-5-nano", alias="MODEL_NAME")
    temperature: float = Field(default=1.0, alias="TEMPERATURE")
    max_tokens: int = Field(default=1500, alias="MAX_TOKENS")

    upload_max_mb: int = Field(default=10, alias="UPLOAD_MAX_MB")
    allowed_origins: str = Field(default="*", alias="ALLOWED_ORIGINS")

    class Config:
        # Look for .env file in the backend directory
        env_file = Path(__file__).parent.parent / ".env"
        env_file_encoding = "utf-8"


settings = Settings()


