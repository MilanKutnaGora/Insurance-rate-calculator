from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base


class Rate(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    cargo_type = Column(String, index=True)
    declared_value = Column(Float)
    rate = Column(Float)


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    action = Column(String)
    timestamp = Column(DateTime)