from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(String)
    date = Column(DateTime)

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer = Column(String)
