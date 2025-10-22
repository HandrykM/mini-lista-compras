from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.service.database import init_db
from app.routes import user, items, stats, shopping_list

app = FastAPI(title=settings.APP_NAME, redirect_slashes=False)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("Conectando a MongoDB...")
    await init_db()
    print("MongoDB conectado correctamente.")

@app.get("/")
async def root():
    return {
        "message": "Mini Lista de Compras API",
        "status": "online",
        "version": "2.0.0"
    }

# Rutas
app.include_router(user.router)  # /auth/*
app.include_router(items.router)  # /items/*
app.include_router(stats.router)  # /stats/*
app.include_router(shopping_list.router)  # /lists/*