from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from .routers import driver

from pydantic import BaseModel
from typing import Optional

app = FastAPI()

app.include_router(driver.router)


@app.get("/")
def root():
    return {"Welcome": "F1 Rest API"}



# class Driver(BaseModel):
#     first_name: str
#     last_name: str
#     nationality: str
#     dob: str
#     url: str
#     comments: Optional[str] = None
#
#
# @app.get("/")
# def root():
#     return {"msg": "Welcome"}
#
#
# @app.get("/driver")
# def get_all_drivers():
#     return data.drivers
#
#
# @app.get("/driver/{driver_id}")
# def get_all_drivers(driver_id: int):
#     return {"driver_id": driver_id, "name": "Some driver"}
#
#
# @app.post("/driver")
# def add_new_driver(driver_details: Driver):
#     return driver_details
#
#
# @app.put("/driver/{driver_id}")
# def update_driver(driver_id: int, first_name: Optional[str] = Query(None, max_length=50)):
#     result = {"driver_id": driver_id, "msg": "Driver updated"}
#     if first_name:
#         result.update({"first_name": first_name})
#     return result
#
#
# @app.delete("/driver/{driver_id}")
# def delete_driver(driver_id: int):
#     return {"driver_id": driver_id, "msg": "Driver deleted"}


