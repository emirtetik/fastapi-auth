from fastapi.exceptions import HTTPException
from app.core.security import get_password_hash
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import CreateUserRequest
from sqlalchemy.orm import Session

async def create_user_account(data: CreateUserRequest, db: Session):
    existing_user = UserRepository.get_user_by_email(db, data.email)
    if existing_user:
        raise HTTPException(status_code=422, detail="Email is already registered with us.")
    hashed_password = get_password_hash(data.password)
    new_user = UserRepository.create_user(db, data, hashed_password)
    return new_user 

async def login_user(data, db: Session):
    user, access_token = UserRepository.authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "registered_at": user.registered_at
        }
    }