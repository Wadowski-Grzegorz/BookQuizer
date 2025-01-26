from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.recommendation_service import get_recommended_book

router = APIRouter()

@router.post("/")
def recommend(numbers: List[float], db: Session = Depends(get_db)):
    return get_recommended_book(numbers, db)
