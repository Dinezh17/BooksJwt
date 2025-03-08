from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Book(BaseModel):
    title: str
    author: str
    published_year: int


users_db = {}
books_db = {}
book_id_counter = 1
