from jose import JWTError,jwt
import os
from datetime import datetime,timedelta
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
load_dotenv()

Oauth2=OAuth2PasswordBearer(tokenUrl='login')
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    to_encode.update({"exp":expire})
    access_token=jwt.encode(to_encode,os.getenv('SECRET_KEY'),algorithm=os.getenv('ALGORITHM'))
    return access_token

def verify(token:str,credential_Exception):
    try:
        payload=jwt.decode(token,os.getenv('SECRET_KEY'),algorithms=[os.getenv('ALGORITHM')])
        user_name=payload.get("user_name")
        print(user_name)
        if user_name==None:
            raise credential_Exception
        email=payload.get("email")
        data= user_name
    except JWTError:
        raise credential_Exception
    return data
def get_current_user(token:str=Depends(Oauth2)):
    credential_exception=HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="InValid Credential",headers={"WWW-Authenticate":"Bearer"})

    return verify(token,credential_exception)

