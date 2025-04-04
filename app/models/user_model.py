from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from datetime import datetime
from app.core.database import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String, unique=True, index=True)
    password = Column(String(100))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    registered_at = Column(DateTime, nullable=True, default=None)