from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.settings import get_settings
from typing import Generator

settings = get_settings()

engine = create_engine(settings.DATABASE_URL,
                       pool_pre_ping=True,
                       pool_recycle=3600,
                       )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()