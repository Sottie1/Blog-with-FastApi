from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas import TokenData
from fastapi import Depends, HTTPException, status


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "180defd06495fe9f43974baf224edfff9b9236f224ae37145b48f99369e9aae1634f36dacf0813caefe7142c6a17f3d2a890958966e5291a90bd76b245f47c0e042288e76aec3575923ac3968b77d00bbc0d7b210631979cd30066b20d45b6ef6f1b814608e2a370f39b324bfbc6991cf403c9801bb223797220d30956266e839fe6f73baaae0c56b50a00f36022335797767aced38e9e878fd1fb578b97f8bbb665311a301f6f6ae0771014d8749c9d40bf2fd5454030e84caecf25992b7a19cb121b9cbdf3290caf95aab81dea42b792b8679ca5106dfda00d5a56b84d80fccc4d7d1972c0c8e7a8e1da44c224a0a61721d26198a245c41691090562304116"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user =db.query(models.User).filter(models.User.username == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user