from fastapi import FastAPI, Depends
from app.core.database import engine, Base, get_db
from typing import Annotated
from sqlalchemy.orm import Session
from app.api.routes import router 

Base.metadata.create_all(bind=engine)

app = FastAPI()

db_dependency = Annotated[Session, Depends(get_db)]

app.include_router(router)
