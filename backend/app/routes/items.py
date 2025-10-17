from fastapi import APIRouter, HTTPException
from database import db
from models import ItemModel
from schemas import item_entity, items_entity
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_items():
    items = await db.items.find().to_list(100)
    return items_entity(items)

@router.post("/")
async def create_item(item: ItemModel):
    new_item = item.dict()
    res = await db.items.insert_one(new_item)
    created = await db.items.find_one({"_id": res.inserted_id})
    return item_entity(created)

@router.put("/{id}")
async def update_item(id: str, item: ItemModel):
    await db.items.update_one({"_id": ObjectId(id)}, {"$set": item.dict()})
    updated = await db.items.find_one({"_id": ObjectId(id)})
    if not updated:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return item_entity(updated)

@router.delete("/{id}")
async def delete_item(id: str):
    result = await db.items.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"mensaje": "Item eliminado"}
