def item_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nombre": item["nombre"],
        "cantidad": item["cantidad"],
        "estado": item["estado"],
    }

def items_entity(items) -> list:
    return [item_entity(i) for i in items]
