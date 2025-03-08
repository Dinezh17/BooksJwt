from pydantic import BaseModel

users_db = {}  

class UserCreate(BaseModel):
    username: str
    password: str