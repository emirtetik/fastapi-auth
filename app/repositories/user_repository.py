from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user_model import UserModel
from app.schemas.user_schema import CreateUserRequest
from app.core.security import verify_password, create_access_token

class UserRepository:
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(UserModel).filter(UserModel.email == email).first()

    @staticmethod
    def create_user(db: Session, user_data: CreateUserRequest, hashed_password: str):
        new_user = UserModel(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password=hashed_password,
            registered_at=datetime.now(),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        user = UserRepository.get_user_by_email(db, email)
        if not user or not verify_password(password, user.password):
            return None
        access_token = create_access_token(data={"sub": user.email})
    
        return user, access_token