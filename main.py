from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep
from typing import List
app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id:int):
    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    db.data[sheep.id] = sheep
    return sheep

@app.get("/sheep/", response_model=List[Sheep])
def get_all_sheep():
    return db.read_all()

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):
    deleted_sheep = db.delete_sheep(id)
    if not deleted_sheep:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return None
