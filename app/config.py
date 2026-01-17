from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY:str
    ALGORITHM:str
    SERVER:str
    DB_NAME:str
    ACCESS_TOKEN_EXPIRE_MINUTES:str
settings=Settings()


    




