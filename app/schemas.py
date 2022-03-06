from pydantic import BaseModel


class DriverBase(BaseModel):
    first_name: str
    last_name: str
    nationality: str
    dob: str
    url: str


class DriverCreate(DriverBase):
    pass


class DriverOut(DriverBase):
    id: int

    class Config:
        orm_mode = True
