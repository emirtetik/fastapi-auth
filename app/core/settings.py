from functools import lru_cache
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    DEBUG: bool = bool(os.environ.get("DEBUG", False))
    USE_CREDENTIALS: bool = os.getenv("USE_CREDENTIALS", "False").lower() in ("true", "1", "t")

    FRONTEND_HOST: str = os.environ.get("FRONTEND_HOST", "http://localhost:3000")
    # Veritabanı Ayarları
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "password")
    DATABASE_DB: str = os.getenv("DATABASE_DB", "AppDB")
    DATABASE_PORT: int = int(os.getenv("DATABASE_PORT", 5432))
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    

    
    # Güvenlik Ayarları
    JWT_SECRET: str = os.getenv("JWT_SECRET", "default_jwt_secret")
    JWT_ALGORITHM: str = os.environ.get("ACCESS_TOKEN_ALGORITHM", "HS256")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE: int = int(os.environ.get("ACCESS_TOKEN_EXPIRE", 3))
    REFRESH_TOKEN_EXPIRE: int = int(os.environ.get("REFRESH_TOKEN_EXPIRE", 1440))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    
@lru_cache()
def get_settings() -> Settings:
    return Settings()