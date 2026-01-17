from fastapi import APIRouter,HTTPException,status,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schemas,models,utils
from sqlalchemy.orm import Session
from ..database import get_db
from .. import oauth2,schemas

router=APIRouter()

@router.post('/login',response_model=schemas.Token)
def user_login(user_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    name=user_data.username
    user=db.get(models.User,name)
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found or Chutiye Sahi User_name Daal  !")
    elif not utils.verify(user_data.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="ABE Gaandu Sahi Password Daal  !")
    token=oauth2.create_access_token({'user_name':user.user_name,'email':user.email})
    return {'access_token':token,"token_type":"bearer"}
    
