import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from . import models
from .database import engine
from .routers import posts, users, login, vote
load_dotenv()
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "templates")

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory=templates_path)

@app.get('/')
def root(request: Request):
    # Just use "home.html". NOT "/templates/home.html"
    return templates.TemplateResponse("home.html", {"request": request})

app.include_router(vote.router)
app.include_router(login.router)
app.include_router(posts.router)
app.include_router(users.router)


