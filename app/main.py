from fastapi import FastAPI, Depends
from pydantic import BaseModel
from app.core.database import engine, SessionLocal, Base
from typing import Annotated
from sqlalchemy.orm import Session
import app.models
from app.api.routes import router 

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

app.include_router(router)
