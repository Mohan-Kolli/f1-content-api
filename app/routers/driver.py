from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Response
from typing import Optional, List, Dict
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db

router = APIRouter(
    prefix="/driver"
)


@router.get("", response_model=list[schemas.DriverOut])
def get_drivers(db: Session = Depends(get_db)):
    return db.query(models.Driver).all()


@router.get("/{driver_id}", response_model=schemas.DriverOut)
def get_driver_by_id(driver_id: int, db: Session = Depends(get_db)):
    driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if not driver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Driver with {driver_id} not found")
    return driver


# TODO Add conditions to stop duplicate driver entries*
@router.post("", response_model=schemas.DriverOut)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    new_driver = models.Driver(**driver.dict())
    db.add(new_driver)
    db.commit()
    db.refresh(new_driver)
    return new_driver


@router.put("/{driver_id")
def update_driver(driver_id: int, db: Session = Depends(get_db)):
    pass


@router.delete("/{driver_id}")
def delete_driver(driver_id: int, db: Session = Depends(get_db)):
    remove_driver = db.query(models.Driver).filter(models.Driver.id == driver_id).first()
    if not remove_driver:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Driver with id: {driver_id} was not found")

    db.delete(remove_driver)
    db.commit()
    return Response(status_code=status.HTTP_200_OK, content="Driver deleted successfully")


