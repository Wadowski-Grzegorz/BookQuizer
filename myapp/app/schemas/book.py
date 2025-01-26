from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    calc_book: float

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
