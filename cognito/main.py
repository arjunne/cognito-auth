from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from cognito import signup, confirm_signup, authenticate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str
    password: str
    email: str

@app.post("/signup")
async def user_signup(user: User):
    response = signup(user.username, user.password, user.email)
    if type(response) == str:
        raise HTTPException(status_code=400, detail=response)
    else:
        return {"message": "User signed up successfully."}

class Confirmation(BaseModel):
    username: str
    code: str

@app.post("/confirm")
async def user_confirm(confirmation: Confirmation):
    response = confirm_signup(confirmation.username, confirmation.code)
    if type(response) == str:
        raise HTTPException(status_code=400, detail=response)
    else:
        return {"message": "User confirmed successfully."}

class Login(BaseModel):
    username: str
    password: str

@app.post("/login")
async def user_login(login: Login):
    response = authenticate(login.username, login.password)
    if type(response) == str:
        raise HTTPException(status_code=400, detail=response)
    else:
        return {"access_token": response['AccessToken']}
