from sqlalchemy.orm import Session
from . import models, schemas

def create_rate(db: Session, rate: schemas.RateCreate):
    db_rate = models.Rate(**rate.dict())
    db.add(db_rate)
    db.commit()
    db.refresh(db_rate)
    return db_rate

def get_rate(db: Session, cargo_type: str):
    return db.query(models.Rate).filter(models.Rate.cargo_type == cargo_type).first()

def delete_rate(db: Session, rate_id: int):
    db.query(models.Rate).filter(models.Rate.id == rate_id).delete()
    db.commit()