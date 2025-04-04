from pydantic import BaseModel, EmailStr

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    
class LoginUserRequest(BaseModel):
    email: EmailStr
    password: str