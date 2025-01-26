from pydantic import BaseModel
from typing import List

class RecommendationRequest(BaseModel):
    numbers: List[float]

class RecommendationResponse(BaseModel):
    id: int
    title: str
    calc_book: float
