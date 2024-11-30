from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RateBase(BaseModel):
    cargo_type: str
    declared_value: float
    rate: float

class RateCreate(RateBase):
    pass

class Rate(RateBase):
    id: int

    class Config:
        orm_mode = True

class CalculateInsurance(BaseModel):
    cargo_type: str
    declared_value: float

class InsuranceCost(BaseModel):
    insurance_cost: float

class LogBase(BaseModel):
    user_id: Optional[int] = None
    action: str
    timestamp: datetime

class LogCreate(LogBase):
    pass

class Log(LogBase):
    id: int

    class Config:
        orm_mode = True