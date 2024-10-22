
from sqlalchemy.orm import Session
from . import models, schemas
from typing import List

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.clientid == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100) -> List[models.Client]:
    return db.query(models.Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas.ClientBase):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_dish(db: Session, dish_id: int):
    return db.query(models.Dish).filter(models.Dish.dishid == dish_id).first()

def get_dishes(db: Session, skip: int = 0, limit: int = 100) -> List[models.Dish]:
    return db.query(models.Dish).offset(skip).limit(limit).all()

def create_dish(db: Session, dish: schemas.DishBase):
    db_dish = models.Dish(**dish.dict())
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return db_dish

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.orderid == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 100) -> List[models.Order]:
    return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderBase):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order_id: int, order: schemas.OrderBase):
    db_order = db.query(models.Order).filter(models.Order.orderid == order_id).first()
    if db_order:
        for key, value in order.dict().items():
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.orderid == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order