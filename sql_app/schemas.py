from pydantic import BaseModel
from typing import Optional


class DriverBase(BaseModel):
    first_name: str
    last_name: str
    nationality: str
    dob: str
    url: str


class DriverCreate(DriverBase):
    pass


class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True


