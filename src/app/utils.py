from pydantic import BaseModel, Field
import bcrypt


# salt = '$2b$12$w9cNaVtJI1ofOlUUrBb3ge'

class Login(BaseModel):
    login: str
    password: str

class ImgString(BaseModel):
    img_string: str = Field(
        None, title="The string for image generation", min_length=3, max_length=40
    )


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), '$2b$12$w9cNaVtJI1ofOlUUrBb3ge'.encode('utf-8'))

