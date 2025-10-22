from typing import Optional, Dict, Any
from beanie import PydanticObjectId
from backend.app.models import User

async def crear_usuario(user: User) -> User:
    await user.insert()
    return user

async def actualizar_usuario(user_id: PydanticObjectId, data: Dict[str, Any]) -> Optional[User]:
    user = await User.get(user_id)
    if not user:
        return None
    # No permitir campos protegidos
    data.pop("id", None)
    data.pop("created_at", None)

    for k, v in data.items():
        setattr(user, k, v)
    await user.save()
    return user

async def eliminar_usuario(user_id: PydanticObjectId) -> bool:
    user = await User.get(user_id)
    if not user:
        return False
    await user.delete()
    return True
