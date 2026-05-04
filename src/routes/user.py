from fastapi import APIRouter, HTTPException, status

from sqlalchemy import select

from src.dependencies.db_dependency import db_dependency
from src.schemas.user import UserIn, UserOut
from src.models.users import User
from src.core.security import hash_password

router = APIRouter(prefix="/user",
                   tags=["user"])

@router.post("/create", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user_to_create: UserIn,
                      db: db_dependency):
    
    stmt = select(User.id).where(User.email == user_to_create.email)
    result = await db.execute(stmt)
    user_exists = result.scalar_one_or_none()

    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="email already in use")

    user_created = User(name = user_to_create.name,
                        email = user_to_create.email,
                        password_hash = hash_password(user_to_create.password))
    
    db.add(user_created)
    await db.commit()
    await db.refresh(user_created)

    return user_created