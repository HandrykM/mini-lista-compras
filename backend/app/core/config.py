from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Mini Lista de Compras"
    DEBUG: bool = True

    # MongoDB
    MONGO_URI: str = "mongodb://localhost:27017"  # o tu cadena de Atlas desde .env
    DB_NAME: str = "shop_fast"

    # JWT
    SECRET_KEY: str = "cambiaesta"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Pydantic Settings v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

settings = Settings()
