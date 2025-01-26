from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.services.recommendation_service import get_recommended_book
from app.schemas import recommendation as schemas

router = APIRouter()

@router.post("/", response_model=schemas.RecommendationResponse)
def recommend(request: schemas.RecommendationRequest, db: Session = Depends(get_db)):
    return get_recommended_book(request.answers, db)
