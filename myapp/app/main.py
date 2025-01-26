from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import recommendation, book
from app.database import init_db


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adresy, które mogą wykonywać zapytania
    allow_credentials=True,
    allow_methods=["*"],  # Zezwalaj na wszystkie metody (GET, POST, itp.)
    allow_headers=["*"],  # Zezwalaj na wszystkie nagłówki
)

app.include_router(recommendation.router, prefix="/recommendation", tags=["recommendations"])
app.include_router(book.router, prefix="/book", tags=["books"])


# Create and add books if doesn't exist
@app.on_event("startup")
def on_startup():
    init_db()





