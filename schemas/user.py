"""User schemas."""

from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator
from typing import Self
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

    @field_validator("password")
    @classmethod
    def password_bytes(cls, value: str) -> str:
        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password must not exceed 72 UTF-8 bytes")
        return value


class UserRead(BaseModel):
    id: int
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None

    @model_validator(mode="after")
    def validate_email(self) -> Self:
        if "email" in self.model_fields_set and self.email is None:
            raise ValueError("Email cannot be null")
        return self
