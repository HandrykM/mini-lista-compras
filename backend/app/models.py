from pydantic import BaseModel
from typing import Optional

class ItemModel(BaseModel):
    id: Optional[str]
    nombre: str
    cantidad: int
    estado: str  # "pendiente" o "comprado"
