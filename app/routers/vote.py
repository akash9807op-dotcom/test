from fastapi import APIRouter,HTTPException,status,Depends
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db
from .. import oauth2,schemas

router=APIRouter()

@router.post('/post/like')  # post_id is path parameter which should be named and use in function defination
def Vote(details:schemas.Vote,db:Session=Depends(get_db),user=Depends(oauth2.get_current_user)):
    print("Hellow")
    post=db.get(models.Vote,(details.id,user))
    if post==None:
        post=models.Vote(post_id=details.id,user_name=user,direc=details.direc)
        db.add(post)
        db.commit()
    else:
        post.direc=details.direc
        db.commit()
    return "successfully done"
