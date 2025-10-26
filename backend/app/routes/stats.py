from fastapi import APIRouter, HTTPException
from app.schemas import StatsResponse
from app.repository.stats_repository import snapshot_stats

router = APIRouter(
    prefix="/stats",
    tags=["Stats"]
)

@router.get("/", response_model=StatsResponse)
async def get_stats():
    """
    Retorna estadísticas generales sobre los ítems en la base de datos.
    """
    try:
        data = await snapshot_stats()
        return StatsResponse.model_validate(data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener estadísticas: {e}")
