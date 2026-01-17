from pydantic import BaseModel,EmailStr
from datetime import datetime
class BasePosts(BaseModel):
    title:str
    content:str
    published:bool=False
    user_name:str
class Vote(BaseModel):
    id:int
    direc:int
class UserIN(BaseModel):
    user_name:str
    email:EmailStr
    password:str
class CreatePost(BasePosts):
    pass
class PostOUT(BaseModel):
    id:int
    title:str
    content:str
    created_at:datetime
    user_name:str
    user:UserIN
    likes:int
    dislikes:int
    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    user_name:str
    password:str
class UserOUT(BaseModel):
    user_name:str
    email:EmailStr
class Token(BaseModel):
    access_token:str
    token_type:str
class tokenData(BaseModel):
    pass 



