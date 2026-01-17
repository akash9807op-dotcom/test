from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import posts,users,login,vote
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
models.Base.metadata.create_all(bind=engine)
current_dir = os.path.dirname(os.path.abspath(__file__))

app=FastAPI()# app is instance of fastapi application 

origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/')
def root(request:Request):
    return templates.TemplateResponse("/templates/home.html", {"request": request})
app.include_router(vote.router)
app.include_router(login.router)
app.include_router(posts.router)
app.include_router(users.router)


# git command to commit and push into git
# git add --all
# git commit -m "added new feature"   contian the commit name
# git push origin main      to push all in orgin main



    
    

    










































# class Post(BaseModel):
#     title:str
#     content:str
#     published:bool=True
# @app.get('/')
# def home():
#     return "hellllllooooo"
# @app.post('/h')
# def x(new_post:Post):
# # new_post is a Pydantic model created from the request body.
# # It validates the incoming data and converts it to a Python object.
# # Use new_post.dict() to access the data as a dictionary.
#     if new_post.published==False:
#         return f" Hey  {new_post.title}\n why you dont want to published"
#     return f"Hey {new_post.title} {new_post.content} why did you published this------"
# from fastapi import FastAPI
# app = FastAPI()



# @app.post("/items/")
# def read_item():
#     return {"item_id":"34"}
# @app.get("/items/")
# def read_item():
#     return {"item_id":"35"}

# # The Database
# my_posts = [{"id": 1, "title": "Top post", "content": "check out this content"}]

# @app.get("/posts/{id}")
# def get_post(id: int):
#     # Logic to find the post
#     for post in my_posts:
#         if post["id"] == id:
#             return post
    
#     # If the loop finishes and we didn't find the ID...
#     return {"message": "Post not found"}



