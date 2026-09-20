"""Item schemas."""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ItemCreate(BaseModel):
    title: str
    description: str = ""


class ItemRead(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
