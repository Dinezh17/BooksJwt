from fastapi import HTTPException
from auth import hash_password, verify_password
from models import users_db

def register_user(username: str, password: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    users_db[username] = hash_password(password)
    return {"message": "User registered successfully"}

def authenticate_user(username: str, password: str):
    if username not in users_db or not verify_password(password, users_db[username]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return username
