
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os

SQLALCHEMY_DATABASE_URL =f"postgresql://{os.getenv('USER_NAME')}:{os.getenv('PASSWORD')}@{os.getenv('ADDRESS')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine=create_engine(SQLALCHEMY_DATABASE_URL,echo=True)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
