from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os



DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Funkcja do uzyskania sesji
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    from app.models.book import Book
    from app.schemas.book import BookCreate
    from app.crud.book import create_book

    db = SessionLocal()

    try:
        # Create all tables in the database (if they don't exist)
        Base.metadata.create_all(bind=engine)
        
        # Check if the book table is empty
        books_count = db.query(Book).count()
        
        if books_count < 4:
            # If no books are found, add sample books
            sample_books = [
                BookCreate(title="The Catcher in the Rye", calc_book=9.12),
                BookCreate(title="To Kill a Mockingbird", calc_book=4.5),
                BookCreate(title="1984", calc_book=7),
                BookCreate(title="Moby Dick", calc_book=1.2),
                BookCreate(title="Pride and Prejudice", calc_book=3),
            ]
            
            # Create and add the books to the database
            for book in sample_books:
                create_book(db, book)
                
            print("Sample books added to the database.")
    
    finally:
        db.close()    