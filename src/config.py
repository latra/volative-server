from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv()
class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()
