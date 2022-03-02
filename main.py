from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Welcome"}


@app.get("/driver")
def get_all_drivers():
    return {"drivers": "all"}


@app.get("/driver/{driver_id}")
def get_all_drivers(driver_id: int):
    return {"driver_id": driver_id, "name": "Some driver"}


@app.post("/driver")
def add_new_driver():
    return {"msg": "new driver added"}


@app.put("/driver/{driver_id}")
def update_driver(driver_id: int):
    return {"driver_id": driver_id, "msg": "Driver updated"}


@app.delete("/driver/{driver_id}")
def delete_driver(driver_id: int):
    return {"driver_id": driver_id, "msg": "Driver deleted"}


