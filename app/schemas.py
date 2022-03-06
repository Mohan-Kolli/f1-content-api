from pydantic import BaseModel
from datetime import date


class DriverBase(BaseModel):
    first_name: str
    last_name: str
    nationality: str
    dob: date
    url: str


class DriverCreate(DriverBase):
    pass


class DriverOut(DriverBase):
    id: int

    class Config:
        orm_mode = True
