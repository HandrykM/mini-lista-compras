from fastapi import APIRouter, HTTPException, status, Response
from beanie import PydanticObjectId
from passlib.context import CryptContext
from backend.app.models import User
from backend.app.repository.users_repository import crear_usuario, actualizar_usuario, eliminar_usuario
from backend.app.schemas import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Crear usuario
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create(user: UserCreate):
    exists = await User.find_one(User.email == user.email)
    if exists:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    hashed = pwd_context.hash(user.password)
    nuevo = User(username=user.username, email=user.email, password=hashed)
    creado = await crear_usuario(nuevo)
    return UserResponse.model_validate(creado, from_attributes=True)

# Actualizar usuario
@router.put("/{user_id}", response_model=UserResponse)
async def update(user_id: PydanticObjectId, update: UserUpdate):
    data = update.model_dump(exclude_unset=True)
    if "password" in data:
        data["password"] = pwd_context.hash(data["password"])
    updated_user = await actualizar_usuario(user_id, data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return UserResponse.model_validate(updated_user, from_attributes=True)

# Eliminar usuario
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: PydanticObjectId):
    deleted = await eliminar_usuario(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

