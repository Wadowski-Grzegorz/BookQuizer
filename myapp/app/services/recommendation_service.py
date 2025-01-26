from sqlalchemy.orm import Session
import numpy as np
from fastapi import HTTPException
from app.models.book import Book
from app.schemas.recommendation import RecommendationResponse

def get_recommended_book(numbers: list[float], db: Session) -> RecommendationResponse:
    if not numbers:
        raise HTTPException(status_code=400, detail="List of numbers cannot be empty")

    mean_value = np.mean(numbers)
    
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found in the database")
    
    recommended_book = min(books, key=lambda book: abs(book.calc_book - mean_value))

    return RecommendationResponse(
        id=recommended_book.id,
        title=recommended_book.title,
        calc_book=recommended_book.calc_book
    )
