from fastapi import FastAPI, APIRouter, Depends
from typing import Optional, List
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db


router = APIRouter(
    prefix="/driver",
    tags=['Drivers']
)


@router.get("/")
def get_drivers(drive: schemas.DriverCreate, db: Session = Depends(get_db)):
    print("inside driver route")
    print(db.query(models.Driver).all())
    pass
