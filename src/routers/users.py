from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, models, services.auth as auth
from database import get_db
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from repository import UserRepository
from models import User as DBUser
user_router = APIRouter()
user_repository = UserRepository()

@user_router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, password=hashed_password, email=user.email)
    user = user_repository.register_user(db, db_user)
    return schemas.UserResponse.model_validate(user)

@user_router.post("/login", response_model=schemas.Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    db_user : DBUser = user_repository.get_by_username(db, form_data.username)
    if not db_user or not auth.verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Generar el token JWT
    access_token_expires = timedelta(minutes=30)
    access_token = auth.create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
