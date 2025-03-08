from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
from models import Base
import schemas
from auth import create_access_token, get_current_user, register_user, authenticate_user
from userfunctions import list_books, add_book, get_book, update_book, delete_book



Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/", response_model=dict)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@app.post("/login/", response_model=dict)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    username = authenticate_user(db, user)
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected/")
def protected_endpoint(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}. You have access to this protected endpoint."}
@app.get("/books/", response_model=List[schemas.BookResponse])
def list_all_books(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return list_books(db)
@app.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return add_book(db, book)

@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return get_book(db, book_id)

@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book_info(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return update_book(db, book_id, book)

@app.delete("/books/{book_id}", response_model=dict)
def delete_book_info(book_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return delete_book(db, book_id)
