import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

# Internal imports
from . import models
from .database import engine
from .routers import posts, users, login, vote

load_dotenv()

models.Base.metadata.create_all(bind=engine)

# --- FIX START: Create Absolute Paths ---
# Get the location of THIS file (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Create full paths to static and templates
static_path = os.path.join(current_dir, "static")
templates_path = os.path.join(current_dir, "templates")
# --- FIX END ---

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use the absolute paths we created above
app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_path)

@app.get('/')
def root(request: Request):
    # Just use "home.html". NOT "/templates/home.html"
    return templates.TemplateResponse("home.html", {"request": request})

app.include_router(vote.router)
app.include_router(login.router)
app.include_router(posts.router)
app.include_router(users.router)
