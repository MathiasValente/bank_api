from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from passlib.context import CryptContext

from sqlalchemy import select

from src.core.config import env_vars
from src.dependencies.db_dependency import db_dependency

from src.models.users import User

pwd_context = CryptContext(schemes=["argon2"],
                           deprecated="auto")

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