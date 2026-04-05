from pydantic import BaseModel, EmailStr
from typing import Optional

# For creating user
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role: str = "viewer"

# For updating user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None

# For response
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool

    class Config:
        from_attributes = True