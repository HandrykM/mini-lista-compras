# backend/app/main.py
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.core.config import settings
from app.models import User, Item, Stats, ShoppingList

# Importar rutas
from app.routes import items, shopping_list, stats, user, auth

_client: AsyncIOMotorClient | None = None

# URI y DB (pueden venir de variables de entorno)
MONGO_URI = os.getenv("MONGO_URI", settings.MONGO_URI)
DB_NAME = os.getenv("DB_NAME", settings.DB_NAME)

app = FastAPI(title="Mini Lista de Compras - MiniList JH")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
app.include_router(auth.router)  # Ruta de autenticación
app.include_router(user.router)
app.include_router(items.router)
app.include_router(shopping_list.router)
app.include_router(stats.router)

# Root simple
@app.get("/")
async def root():
    return {
        "message": "API Mini Lista de Compras - MiniList JH activa!",
        "version": "1.0.0",
        "docs": "/docs"
    }
