from fastapi import FastAPI, Depends
from auth import create_access_token, get_current_user
from userfunctions import register_user, authenticate_user, list_books, add_book, get_book, update_book, delete_book
from models import User, Book

app = FastAPI()

@app.post("/register/")
def register(user: User):
    return register_user(user)

@app.post("/login/")
def login(user: User):
    username = authenticate_user(user)
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected/")
def protected_endpoint(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}. You have access to this protected endpoint."}


@app.get("/books/")
def list_all_books(current_user: str = Depends(get_current_user)):
    return list_books()

@app.post("/books/")
def create_book(book: Book, current_user: str = Depends(get_current_user)):
    return add_book(book)

@app.get("/books/{book_id}")
def read_book(book_id: int, current_user: str = Depends(get_current_user)):
    return get_book(book_id)

@app.put("/books/{book_id}")
def update_book_info(book_id: int, book: Book, current_user: str = Depends(get_current_user)):
    return update_book(book_id, book)

@app.delete("/books/{book_id}")
def delete_book_info(book_id: int, current_user: str = Depends(get_current_user)):
    return delete_book(book_id)
