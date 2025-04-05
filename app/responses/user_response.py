from typing import Optional
from pydantic import EmailStr, BaseModel
from app.responses.base_response import BaseResponse
from datetime import datetime

class UserData(BaseResponse):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    registered_at: Optional[datetime] = None
    
class LoginUserData(BaseModel):
    access_token: str
    token_type: str
    user: UserData

class UserLoginResponse(BaseModel):
    status: str = "success"
    message: str
    data: LoginUserData

class UserRegisterResponse(BaseModel):
    status: str = "success"
    message: str
    data: UserData