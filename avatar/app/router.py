from fastapi import APIRouter, Response, Path
from functions import creation
import base64
from io import BytesIO
import jwt


router = APIRouter()

@router.get("/avatar/{img_string}")
async def get_avatar(img_string: str = Path(..., title="The string to turn into an avatar", min_length=3, max_length=50)):

    img = creation(img_string)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = "data:image/png;base64,"+(base64.b64encode(buffered.getvalue())).decode("utf-8")
    return Response(content=img_str, media_type="base64")
