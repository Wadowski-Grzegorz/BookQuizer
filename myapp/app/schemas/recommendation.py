from pydantic import BaseModel
from typing import List

class RecommendationResponse(BaseModel):
    id: int
    title: str
    calc_book: float

class RecommendationRequest(BaseModel):
    answers: List[float]
