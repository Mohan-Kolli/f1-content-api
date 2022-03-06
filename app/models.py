from sqlalchemy import Integer, String, Column, Date
from .database import Base


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    nationality = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    url = Column(String, nullable=True)