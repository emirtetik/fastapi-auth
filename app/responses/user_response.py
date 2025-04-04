from typing import Union
from pydantic import EmailStr, BaseModel
from app.responses.base_response import BaseResponse
from datetime import datetime

class UserResponse(BaseResponse):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    registered_at: Union[None, datetime] = None
    