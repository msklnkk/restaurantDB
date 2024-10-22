
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientBase, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)

@app.get("/clients/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients

@app.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    db_client = crud.get_client(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@app.post("/dishes/", response_model=schemas.Dish)
def create_dish(dish: schemas.DishBase, db: Session = Depends(get_db)):
    return crud.create_dish(db=db, dish=dish)

@app.get("/dishes/", response_model=List[schemas.Dish])
def read_dishes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dishes = crud.get_dishes(db, skip=skip, limit=limit)
    return dishes

@app.get("/dishes/{dish_id}", response_model=schemas.Dish)
def read_dish(dish_id: int, db: Session = Depends(get_db)):
    db_dish = crud.get_dish(db, dish_id=dish_id)
    if db_dish is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return db_dish

@app.post("/orders/", response_model=schemas.Order)
def create_order(order: schemas.OrderBase, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@app.get("/orders/", response_model=List[schemas.Order])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders

@app.get("/orders/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.put("/orders/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderBase, db: Session = Depends(get_db)):
    updated_order = crud.update_order(db, order_id=order_id, order=order)
    if updated_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order

@app.delete("/orders/{order_id}", response_model=schemas.Order)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.delete_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
