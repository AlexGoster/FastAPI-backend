"""Item schemas."""

from pydantic import BaseModel, Field, model_validator
from typing import Self
from datetime import datetime
from typing import Optional


class ItemCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = ""


class ItemRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ItemUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=255)
    description: Optional[str] = None

    @model_validator(mode="after")
    def validate_title(self) -> Self:
        if "title" in self.model_fields_set and self.title is None:
            raise ValueError("Title cannot be null")
        return self
