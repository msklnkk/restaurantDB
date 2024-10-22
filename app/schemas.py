from pydantic import BaseModel
from typing import Optional
from datetime import date

class ClientBase(BaseModel):
    name: str
    phone_number: Optional[str] = None
    mail: Optional[str] = None
    discount_percentage: Optional[int] = None

class Client(ClientBase):
    clientid: int
    class Config:
        orm_mode = True

class DishBase(BaseModel):
    name: str
    type: Optional[str] = None
    recipe: Optional[str] = None

class Dish(DishBase):
    dishid: int
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    tableid: Optional[int] = None
    order_date: date
    total_sum: float
    status: str
    staffid: Optional[int] = None
    clientid: Optional[int] = None
    payment_method: Optional[str] = None

class Order(OrderBase):
    orderid: int
    class Config:
        orm_mode = True