from fastapi import APIRouter, Response, Path
import base64
from io import BytesIO
import os

if os.environ.get('IS_CONTAINER', False):
    from . import functions
else:
    import functions

router = APIRouter()

@router.get("/avatar/{img_string}")
async def get_avatar(img_string: str = Path(..., title="The string to turn into an avatar", min_length=3, max_length=50)):

    img = functions.creation(img_string)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = "data:image/png;base64,"+(base64.b64encode(buffered.getvalue())).decode("utf-8")
    return Response(content=img_str, media_type="base64")
