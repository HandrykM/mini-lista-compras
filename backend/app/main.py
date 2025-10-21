from fastapi import FastAPI
from backend.app.core.config import settings
from backend.app.service.database import init_db
from backend.app.routes import user, items, stats, shopping_list

app = FastAPI(title=settings.APP_NAME, redirect_slashes=False)

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
