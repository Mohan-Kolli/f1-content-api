from sqlalchemy import Column, Boolean, Integer, String

from .database import Base


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=true)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    nationality = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    url = Column()
