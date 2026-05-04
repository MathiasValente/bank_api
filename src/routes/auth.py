from datetime import timedelta

from fastapi import APIRouter, HTTPException, status

from src.core.security import authenticate_user, create_access_token
from src.dependencies.db_dependency import db_dependency
from src.core.security import form_dependency
from src.schemas.token import Token

router = APIRouter(prefix="/auth",
                   tags=["auth"])

@router.post("/token", response_model=Token)
async def login_for_acces_token(db: db_dependency, form: form_dependency):

    user = await authenticate_user(db,
                                   form.username,
                                   form.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    token = create_access_token(user.email, timedelta(minutes=20))

    return {"access_token": token,
            "token_type": "bearer"}