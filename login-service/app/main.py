from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas, database
from typing import List

app = FastAPI()

# Połączenie z bazą danych
database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()  # Tworzymy sesję
    try:
        yield db
    finally:
        db.close()  # Zamykanie sesji po zakończeniu

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)

@app.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db=db)


