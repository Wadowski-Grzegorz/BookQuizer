from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True) # Title of the book
    calc_book = Column(Float)
