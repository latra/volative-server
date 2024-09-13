from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from models import User
from services.auth import decode_token
from exceptions import credentials_exception, permission_exception
from repository import UserRepository
from enums import Roles
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

user_repository = UserRepository()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    
    payload = decode_token(token)
    if not payload:
        raise credentials_exception
    
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    user = user_repository.get_by_username(db, username)
    if user is None:
        raise credentials_exception
    
    return user

def get_current_admin_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    if user is None:
        raise credentials_exception 
    if not user.is_admin:
        raise permission_exception
    return user
