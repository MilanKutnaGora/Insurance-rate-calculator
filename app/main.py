from fastapi import FastAPI
from app.api.endpoints import insurance, rates
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(insurance.router)
app.include_router(rates.router)



