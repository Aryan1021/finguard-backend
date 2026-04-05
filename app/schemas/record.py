from pydantic import BaseModel
from typing import Optional
from datetime import date

class RecordCreate(BaseModel):
    amount: float
    type: str  # income / expense
    category: str
    date: date
    description: Optional[str] = None
    user_id: int


class RecordUpdate(BaseModel):
    amount: Optional[float] = None
    type: Optional[str] = None
    category: Optional[str] = None
    date: Optional[date] = None
    description: Optional[str] = None


class RecordResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    description: Optional[str]
    user_id: int

    class Config:
        from_attributes = True