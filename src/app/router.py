from fastapi import APIRouter, HTTPException, Header
import jwt
import requests

from . import utils
from . import sql


router = APIRouter()




@router.post('/login')
async def login(login_info: utils.Login):
    DB = sql.Connection()
    user_data = DB.get_user(login_info.login)

    if not user_data:
        raise HTTPException(status_code=400, detail='Incorrect username or password')

    hashed_password = utils.hash_password(login_info.password)

    if hashed_password.decode('utf-8') != user_data[1]:
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    DB.close()
    return jwt.encode({'access_token': login_info.login, 'token_type': 'bearer'}, 'secretverysecret', algorithm='HS256')


#Get avatar from your login (from JWT)
@router.post('/avatar')
async def picture_from_login(authorization: str = Header(None)):
    DB = sql.Connection()
    try:
        encoded_jwt = authorization[7:]
        decoded_jwt = jwt.decode(encoded_jwt, "secretverysecret", algorithms=["HS256"])
        login = decoded_jwt['access_token']
    except:
        raise HTTPException(status_code=403, detail='Incorrect token provided')
    else:
        pic = DB.get_cache(login)
        if pic:
            return {'img': pic[1]}
        else:
            r = requests.get('http://127.0.0.1:8001/avatar/'+login)
            DB.add_cache(login, r.text)
            return {'img': r.text}
    finally:
        DB.close()

#Get avatar from any string (still needed to be authorized)
@router.post('/avatar/any')
async def picture(img_string: utils.ImgString, authorization: str = Header(None)):
    DB = sql.Connection()
    try:
        encoded_jwt = authorization[7:]
        decoded_jwt = jwt.decode(encoded_jwt, "secretverysecret", algorithms=["HS256"])
    except:
        raise HTTPException(status_code=403, detail='Incorrect token provided')
    else:
        if decoded_jwt:
            pic = DB.get_cache(img_string.img_string)
            if pic:
                return {'img': pic[1]}
            else:
                r = requests.get('http://127.0.0.1:8001/avatar/' + img_string.img_string)
                DB.add_cache(img_string.img_string, r.text)
                return {'img': r.text}
        else:
            raise HTTPException(status_code=500, detail='Unknown error')
    finally:
        DB.close()



