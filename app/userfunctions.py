from fastapi import HTTPException
from auth import hash_password, verify_password
from models import users_db, books_db, book_id_counter, User, Book

def register_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[user.username] = hash_password(user.password)
    return {"message": "User registered successfully"}

def authenticate_user(user: User):
    if user.username not in users_db or not verify_password(user.password, users_db[user.username]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return user.username

def list_books():
    return list(books_db.values())

def add_book(book: Book):
    global book_id_counter
    book_id = book_id_counter
    books_db[book_id] = book.dict()
    book_id_counter += 1
    return {"book_id": book_id, "details": book.dict()}

def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

def update_book(book_id: int, book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = book.dict()
    return {"message": "Book updated successfully", "details": book.dict()}

def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    del books_db[book_id]
    return {"message": "Book deleted successfully"}
