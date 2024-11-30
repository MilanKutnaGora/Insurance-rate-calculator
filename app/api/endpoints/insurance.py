from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.kafka_logger import log_action
from datetime import datetime

router = APIRouter()


@router.post("/calculate_insurance")
def calculate_insurance(request: schemas.InsuranceRequest, db: Session = Depends(get_db)):
    rate = crud.get_rate(db, request.date, request.cargo_type)
    if not rate:
        raise HTTPException(status_code=404, detail="Rate not found")

    insurance_cost = request.declared_value * rate.rate

    log_action(request.user_id, "calculate_insurance", str(datetime.now()))

    return {"insurance_cost": insurance_cost}