from fastapi import FastAPI, APIRouter, Depends
from typing import Optional
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db

app = FastAPI()

api_router = APIRouter(
    prefix="/driver"
)


@app.get("/", response_model=schemas.DriverOut)
def get_drivers(drive: schemas.DriverCreate, db: Session = Depends(get_db)):
    return db.query()