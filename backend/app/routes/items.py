# app/routes/items_routes.py

from fastapi import APIRouter, HTTPException, status, Response
from beanie import PydanticObjectId
from backend.app.models import Item
from backend.app.schemas import ItemCreate, ItemResponse, ItemUpdate, ItemPurchase
from backend.app.repository.items_repository import (
    crear_item,
    actualizar_item,
    eliminar_item,
    marcar_item_comprado
)

router = APIRouter(prefix="/items", tags=["Items"])


# Crear un nuevo ítem
@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(payload: ItemCreate):
    item = Item(name=payload.name, quantity=payload.quantity)  # purchased por defecto en el modelo
    creado = await crear_item(item)
    return ItemResponse.model_validate(creado, from_attributes=True)


# Actualizar un ítem
@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: PydanticObjectId, update: ItemUpdate):
    data = update.model_dump(exclude_unset=True)
    updated = await actualizar_item(item_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return ItemResponse.model_validate(updated, from_attributes=True)


# Eliminar ítem
@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: PydanticObjectId):
    ok = await eliminar_item(item_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Marcar ítem como comprado
@router.patch("/{item_id}/purchase", response_model=ItemResponse)
async def mark_purchased(item_id: PydanticObjectId, body: ItemPurchase):
    updated = await marcar_item_comprado(item_id, body.purchased)
    if not updated:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return ItemResponse.model_validate(updated, from_attributes=True)
