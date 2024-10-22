
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Client(Base):
    __tablename__ = "clients"
    clientid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    mail = Column(String)
    discount_percentage = Column(Integer)

class Dish(Base):
    __tablename__ = "dishes"
    dishid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    recipe = Column(String)

class Order(Base):
    __tablename__ = "orders"
    orderid = Column(Integer, primary_key=True, index=True)
    tableid = Column(Integer, ForeignKey("tables.tableid"))
    order_date = Column(Date)
    total_sum = Column(Numeric)
    status = Column(String)
    staffid = Column(Integer, ForeignKey("staff.staffid"))
    clientid = Column(Integer, ForeignKey("clients.clientid"))
    payment_method = Column(String)

class Table(Base):
    __tablename__ = "tables"
    tableid = Column(Integer, primary_key=True, index=True)

class Staff(Base):
    __tablename__ = "staff"
    staffid = Column(Integer, primary_key=True, index=True)
