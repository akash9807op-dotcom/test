from fastapi import HTTPException,status,Depends,APIRouter
from typing import List,Optional
from sqlalchemy.orm import Session # first check if valid post id or not 
from  .. import schemas            #by direction if like then add to table if already there no probelm send messege optinonal
from .. import models,oauth2       # if dislike then go to table and delete it  also check if exit in table or not
from ..database import get_db


router=APIRouter(prefix="/posts",tags=['Post'])

@router.post('/createposts',status_code=status.HTTP_201_CREATED)
def create_posts(posts:schemas.CreatePost,db:Session=Depends(get_db),test_user=Depends(oauth2.get_current_user)):
    post = models.Post(
        title=posts.title,
        content=posts.content,
        published=posts.published,
        user_name=posts.user_name
    )
    db.add(post)
    db.commit()
    return post
# get All Post
@router.get('/')
def get_posts(db:Session=Depends(get_db),test_user=Depends(oauth2.get_current_user),skip:int=0,limit:int=10,search:Optional[str]=""):  
    posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    if posts==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="MESSEGE: No Post Is Posted")
    return posts




# get latest post
@router.get('/latest',response_model=schemas.PostOUT) #remember if this place after get_one_posts then this will case error beacuse order matter 
def get_latest_post(db:Session=Depends(get_db)):
    post_data=db.query(models.Post).order_by(models.Post.id.desc()).first()
    if post_data==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="MESSEGE: There is No Post is Posted")
    return {"data":{post_data}}




# get Post By id
@router.get("/{id}")
def get_one_posts(id:int,db:Session=Depends(get_db),test_user=Depends(oauth2.get_current_user)):
    #use %  for space in search like search=Bombay%2
    post=db.get(models.Post,id)
    likes=db.query(models.Vote).filter(models.Vote.post_id==id ,models.Vote.direc==1).count()#likes = db.query(models.Vote).filter_by(post_id=id, direc=1).all()
    dislikes=db.query(models.Vote).filter(models.Vote.post_id==id ,models.Vote.direc==0).count()
    
    if post==None:
        print("\n",post)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="MESSEGE: id not found")

    return {'post':post,'Likes':likes if likes!=None else 0,'dislikes':dislikes if dislikes!=None else 0}

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),test_user=Depends(oauth2.get_current_user)):
    post=db.get(models.Post,id)
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="id not found or post Does not exit")
    elif post.user_name !=test_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="This Post Does Not Belongs to you ")
    db.delete(post)
    db.commit()
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}',response_model=schemas.PostOUT)
def update_post(id:int,posts:schemas.BasePosts,db:Session=Depends(get_db),test_user=Depends(oauth2.get_current_user)):
    post=db.get(models.Post,id)
    if post==None:
        print("\n",post)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Post Id Enter Valid id or Post does not exit")
    elif post.user_name !=test_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Cannot Update Post ! This Post Does Not Belongs to you ")
    post.title=posts.title
    post.content=posts.content
    post.published=posts.published
    post.user_name=posts.user_name
    db.commit()
    return post




