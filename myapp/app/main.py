from fastapi import FastAPI
from app.controllers import recommendation, book
from app.database import init_db


app = FastAPI()



app.include_router(recommendation.router, prefix="/recommendation", tags=["recommendations"])
app.include_router(book.router, prefix="/book", tags=["books"])


# Create and add books if doesn't exist
@app.on_event("startup")
def on_startup():
    init_db()





