import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models import User, Item, Stats, ShoppingList

_client: AsyncIOMotorClient | None = None

MONGO_URI = os.getenv("MONGO_URI", settings.MONGO_URI)
DB_NAME = os.getenv("DB_NAME", settings.DB_NAME)

app = FastAPI(title="Mi API de Lista de Compras")

async def init_db():
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(MONGO_URI)
    db = _client[DB_NAME]
    await init_beanie(database=db, document_models=[User, Item, Stats, ShoppingList])
    print("Conexión a la base de datos establecida correctamente.")

@app.on_event("startup")
async def startup_event():
    await init_db()

# Endpoint de prueba para la raíz
@app.get("/")
async def root():
    return {"message": "API en funcionamiento!"}
