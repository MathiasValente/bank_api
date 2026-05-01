from datetime import datetime, timedelta, timezone
from typing import Annotated
from jose import jwt, JWTError

from passlib.context import CryptContext

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from sqlalchemy import select

from src.core.config import env_vars
from src.dependencies.db_dependency import db_dependency
from src.models.users import User

pwd_context = CryptContext(schemes=["argon2"],
                           deprecated="auto")

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
form_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]
token_dependency = Annotated[str, Depends(oauth2_bearer)]

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

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str):
    return pwd_context.hash(password)

async def authenticate_user(db: db_dependency,
                            username: str,
                            password: str):
    stmt = select(User).where(User.email == username)
    query_result = await db.execute(stmt)
    user = query_result.scalar_one_or_none()

    if not user:
        return False

    if not verify_password(password, user.password_hash):
        return False
    
    return user

def create_access_token(sub: str, expires_delta: timedelta):
    to_encode = {}
    
    expires = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expires,
                      "sub":sub})

    enconded_jwt =  jwt.encode(to_encode,
                               env_vars.SECRET_KEY,
                               env_vars.ALGORITHM)
    
    return enconded_jwt

def decode_jwt(token: str):
    try:
        payload = jwt.decode(token,
                             env_vars.SECRET_KEY,
                             algorithms=[env_vars.ALGORITHM])
        return payload
    except JWTError:
      return None 