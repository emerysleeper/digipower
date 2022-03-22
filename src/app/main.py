from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import bcrypt
import jwt

app = FastAPI()

# salt = '$2b$12$w9cNaVtJI1ofOlUUrBb3ge'

fake_users_db = {
    "kwaffle": {
        "username": "kwaffle",
        "hashed_password": "$2b$12$w9cNaVtJI1ofOlUUrBb3geFCnLB0N3hTX/j4.XUNrKk3uPvLpc7lK" #"qwerty123"
    },
    "moloko_horol": {
        "username": "moloko_horol",
        "hashed_password": "$2b$12$w9cNaVtJI1ofOlUUrBb3geqIA/U/6ld3/saq817EoYS45fH8rQ42W", #passwordpassword
    },
    "spidermind": {
            "username": "spidermind",
            "hashed_password": "$2b$12$w9cNaVtJI1ofOlUUrBb3ge0LUg2oLdNSXw7SEPz9b0tb9ueuEzkCO", #lolkekcheburek
        },
}


class Login(BaseModel):
    login: str
    password: str


class User(BaseModel):
    username: str
    hashed_password: str


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), '$2b$12$w9cNaVtJI1ofOlUUrBb3ge'.encode('utf-8'))


@app.post("/token")
async def login(login_info: Login):

    user_dict = fake_users_db.get(login_info.login)

    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = User(**user_dict)
    hashed_password = hash_password(login_info.password)

    if hashed_password.decode("utf-8") != user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return jwt.encode({"access_token": user.username, "token_type": "bearer"}, "secretverysecret", algorithm="HS256")