from pydantic import BaseModel, EmailStr, UUID4
from typing import Optional
from models import User
from enums import Roles
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserResponse(UserBase):
    uuid: UUID4
    is_admin: bool
    class Config:
        from_attributes = True
    
class Token(BaseModel):
    access_token: str
    token_type: str


