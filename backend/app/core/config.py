# backend/app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from pydantic import Field, field_validator

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Mini Lista de Compras"
    DEBUG: bool = True

    # MongoDB
    # expose Mongo URI as a real setting so it can be read from .env
    MONGO_URI: str = "mongodb+srv://shop_fast_db:zdTpxhxR5yTwFUnx@shop.z9he8ya.mongodb.net/shop_fast?retryWrites=true&w=majority&appName=Shop"
    DB_NAME: str = "shop_fast"

    # Port (readable from .env)
    PORT: int = 8000

    # JWT
    SECRET_KEY: str = "cambiaesta"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
        
    # CORS
    CORS_ORIGINS: List[str] = Field(
        default_factory=lambda: [
            "http://localhost:8000",
            "http://localhost:8000",
            "http://127.0.0.1:8000",
        ]
    )
    
    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def _parse_cors_origins(cls, v):
        """
        Accept either a JSON array string or a comma-separated string from the .env.
        Examples in .env:
          CORS_ORIGINS='["http://localhost:5173","http://127.0.0.1:5173"]'
          or
          CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
        """
        if isinstance(v, str):
            v = v.strip()
            if not v:
                return []
            try:
                import json
                parsed = json.loads(v)
                if isinstance(parsed, list):
                    return [str(x) for x in parsed]
            except Exception:
                return [s.strip() for s in v.split(",") if s.strip()]
        return v

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
