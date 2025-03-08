from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, get_current_user
from userfunctions import register_user, authenticate_user
from models import UserCreate
app = FastAPI()

@app.get("/")
async def default():
    return {
        "THis is ":" default function call"
    }

@app.post("/register/")
def register(user: UserCreate):
    return register_user(user.username, user.password)

@app.post("/login/")
def login(user: UserCreate):
    username = authenticate_user(user.username, user.password)
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected/")
def protected_endpoint(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}. You have access to this protected endpoint."}
