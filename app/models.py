from sqlalchemy import Column,Integer,String,Boolean,TIMESTAMP,ForeignKey,ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

Base=declarative_base()

class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default='False',nullable=False)
    created_at=Column(TIMESTAMP,server_default=text('now()'),nullable=False)
    user_name=Column(String,ForeignKey("users.user_name",ondelete="CASCADE"),nullable=False)
    user=relationship("User",back_populates="posts")
  

class User(Base):
    __tablename__="users"
    user_name=Column(String,primary_key=True,nullable=False,unique=True)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP,nullable=False,server_default=text('now()'))
    posts=relationship("Post",back_populates="user",cascade="all,delete")

class Vote(Base):
    __tablename__="likes"
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True,nullable=False)
    user_name=Column(String,ForeignKey("users.user_name",ondelete="CASCADE"),primary_key=True,nullable=False)
    direc=Column(Integer,nullable=False)
