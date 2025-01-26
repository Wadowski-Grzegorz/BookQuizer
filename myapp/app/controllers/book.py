from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.crud import book as crud
from app.schemas import book as schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book(db=db, book_id=book_id)

@router.get("/", response_model=List[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db=db)