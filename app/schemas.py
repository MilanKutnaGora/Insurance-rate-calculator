from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class RateBase(BaseModel):
    date: date
    cargo_type: str
    rate: float = Field(..., ge=0, le=1)

class RateCreate(RateBase):
    pass

class RateUpdate(BaseModel):
    date: Optional[date] = None
    cargo_type: Optional[str] = None
    rate: Optional[float] = Field(None, ge=0, le=1)

class Rate(RateBase):
    id: int

    class Config:
        orm_mode = True

class InsuranceRequest(BaseModel):
    date: date
    cargo_type: str
    declared_value: float = Field(..., gt=0)
    user_id: Optional[int] = None

class InsuranceResponse(BaseModel):
    insurance_cost: float

class LogEntry(BaseModel):
    user_id: Optional[int]
    action: str
    timestamp: date

class ErrorResponse(BaseModel):
    detail: str