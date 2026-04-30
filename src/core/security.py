from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from passlib.context import CryptContext

from sqlalchemy import select

from src.core.config import jwt_settings
from src.dependencies.db_dependency import db_dependency

from models.users import User

pwd_context = CryptContext(schemes="bcrypt", deprecated="auto")

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str):
    return pwd_context.hash(password)

async def authenticate_user(db: db_dependency,
                            username: str,
                            password: str):
    stmt = select(User).where(User.name == username)
    query_result = await db.execute(stmt)
    user = query_result.scalar_one_or_none

    if not user:
        return False

    if not verify_password(password, user.password_hash):
        return False

async def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    
    expires = datetime.now(timezone.utc) + expires_delta

    to_encode.update({"exp": expires})

    enconded_jwt =  jwt.encode(to_encode,
                               jwt_settings.SECRET_KEY,
                               jwt_settings.ALGORITHM)
    
    return enconded_jwt

async def decode_jwt(token: str):
    try:
        payload = jwt.decode(token,
                             jwt_settings.SECRET_KEY,
                             algorithms=[jwt_settings.ALGORITHM])
        return payload
    except JWTError:
      return None 