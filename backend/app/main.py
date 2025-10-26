# app/main.py

import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models import User, Item, Stats, ShoppingList

# Importar rutas
from app.routes import items, shopping_list, stats, user

_client: AsyncIOMotorClient | None = None

# URI y DB (pueden venir de variables de entorno)
MONGO_URI = os.getenv("MONGO_URI", settings.MONGO_URI)
DB_NAME = os.getenv("DB_NAME", settings.DB_NAME)

app = FastAPI(title="Mini Lista de Compras")

# Inicialización de la base de datos
async def init_db():
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(MONGO_URI)
    db = _client[DB_NAME]
    await init_beanie(database=db, document_models=[User, Item, Stats, ShoppingList])
    print("Conexión a la base de datos establecida correctamente.")

# Eventos de arranque
@app.on_event("startup")
async def on_startup():
    print("Conectando a MongoDB...")
    try:
        await init_db()
        print("MongoDB conectado correctamente.")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

# Incluyendo rutas
app.include_router(items.router)
app.include_router(shopping_list.router)
app.include_router(stats.router)
app.include_router(user.router)

# Root simple
@app.get("/")
async def root():
    return {"message": "API Mini Lista de Compras activa!"}
