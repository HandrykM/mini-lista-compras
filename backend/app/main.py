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
        "http://127.0.0.1:5173",
        "https://tu-frontend.vercel.app",
        "https://mini-lista-compras.onrender.com"
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

# Rutas
app.include_router(user.router)
app.include_router(items.router)
app.include_router(stats.router)
app.include_router(shopping_list.router)

@app.get("/")
async def root():
    return {
        "message": "Mini Lista de Compras API",
        "status": "online",
        "version": "2.0.0"
    }
