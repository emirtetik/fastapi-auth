from fastapi import APIRouter, status, Depends 
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_schema import CreateUserRequest, LoginUserRequest
from app.services.user_service import create_user_account, login_user

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    new_user = await create_user_account(data, db)

    return {
        "id": new_user.id,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
        "email": new_user.email,
        "registered_at": new_user.registered_at
    }

    
@router.post('/login', status_code=status.HTTP_200_OK)
async def login(data: LoginUserRequest, db: Session = Depends(get_db)):
    return await login_user(data, db)