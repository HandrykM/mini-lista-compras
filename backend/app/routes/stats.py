from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get("/")
async def get_stats():
    total = await db.items.count_documents({})
    comprados = await db.items.count_documents({"estado": "comprado"})
    porcentaje = (comprados / total * 100) if total > 0 else 0
    return {"total": total, "comprados": comprados, "porcentaje": round(porcentaje, 2)}
