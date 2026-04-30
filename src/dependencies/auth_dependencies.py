from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from src.core.security import decode_jwt
from src.dependencies.db_dependency import db_dependency
from src.models.users import User

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

token_dependency = Annotated[str, Depends(oauth2_bearer)]
form_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]

async def get_current_user(token: token_dependency,
                           db: db_dependency):
    payload = decode_jwt(token)

    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid/Expirated Token",
                            headers={"WWW-Authenticate": "Bearer"})
    
    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid Token")        

    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not Found!")

    return user

user_dependency = Annotated[User, Depends(get_current_user)]