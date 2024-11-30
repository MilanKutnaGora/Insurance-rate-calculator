from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.database import get_db
from app.kafka_logger import log_action
from datetime import datetime

router = APIRouter()

@router.post("/rates/", response_model=schemas.Rate)
def create_rate(rate: schemas.RateCreate, db: Session = Depends(get_db)):
    db_rate = crud.create_rate(db=db, rate=rate)
    log_action(None, "create_rate", str(datetime.now()))
    return db_rate

@router.get("/rates/", response_model=List[schemas.Rate])
def read_rates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rates = crud.get_rates(db, skip=skip, limit=limit)
    return rates

@router.get("/rates/{rate_id}", response_model=schemas.Rate)
def read_rate(rate_id: int, db: Session = Depends(get_db)):
    db_rate = crud.get_rate_by_id(db, rate_id=rate_id)
    if db_rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    return db_rate

@router.put("/rates/{rate_id}", response_model=schemas.Rate)
def update_rate(rate_id: int, rate: schemas.RateUpdate, db: Session = Depends(get_db)):
    db_rate = crud.update_rate(db=db, rate_id=rate_id, rate=rate)
    if db_rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    log_action(None, "update_rate", str(datetime.now()))
    return db_rate

@router.delete("/rates/{rate_id}", response_model=schemas.Rate)
def delete_rate(rate_id: int, db: Session = Depends(get_db)):
    db_rate = crud.delete_rate(db=db, rate_id=rate_id)
    if db_rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    log_action(None, "delete_rate", str(datetime.now()))
    return db_rate