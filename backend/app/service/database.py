import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models import User, Item, Stats, ShoppingList

_client: AsyncIOMotorClient | None = None

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "shop_fast")

async def init_db():
    global _client
    try:
        if _client is None:
            _client = AsyncIOMotorClient(settings.MONGO_URI)
        db = _client[settings.DB_NAME]
        await init_beanie(database=db, document_models=[User, Item, Stats, ShoppingList])
        print("Conexión a la base de datos establecida correctamente.")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise