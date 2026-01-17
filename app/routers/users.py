from fastapi import HTTPException,responses,status,Depends,APIRouter
from typing import List
from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from ..database import get_db
from .. import utils
from..import oauth2

router=APIRouter()


@router.post('/createUser',status_code=status.HTTP_201_CREATED)
def createUser(user_data:schemas.UserIN,db:Session=Depends(get_db)):
    new_user=models.User(user_name=user_data.user_name,
                  password=utils.hash(user_data.password),
                  email=user_data.email)
    db.add(new_user)
    db.commit()
    return new_user

@router.get('/users')
def get_all_User(db:Session=Depends(get_db)):
    Users=db.query(models.User).all()
    if len(Users)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="MESSEGE: No User Is Server")
    return Users


@router.get('/users/{user_name}',response_model=schemas.UserOUT)
def get_userby_UserName(user_name:str,db:Session=Depends(get_db)):
    user=db.get(models.User,user_name)
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found or post Does not exit")
    return user
#all post posted by user Login User
@router.get('/user/posts')
def userPost(db:Session=Depends(get_db),user_name=Depends(oauth2.get_current_user)):
    posts=db.query(models.Post).filter(models.Post.user_name==user_name).all()
    if len(posts)==0:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="MESSEGE: No Post Is Posted")
    return posts
#function to update user
# function to delete user-----------
        