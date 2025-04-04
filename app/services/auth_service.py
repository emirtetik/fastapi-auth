# from app.models.user_model import UserModel
# from fastapi.exceptions import HTTPException
# from app.core.security import verify_password
# from app.core.settings import get_settings
# from datetime import timedelta
# from app.responses.user_response import TokenResponse
# from app.core.security import create_access_token

# settings = get_settings()

# async def get_token(data, db):
#     user = db.query(UserModel).filter(UserModel.email == data.username).first()
    
#     if not user:
#         raise HTTPException(
#             status_code=400,
#             detail="Email is not registered with us.",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
    
#     if not verify_password(data.password, user.password):
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid Login Credentials.",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
    
#     _verify_user_access(user=user)
    
#     return await _get_user_token(user=user)
    
    
# def _verify_user_access(user: UserModel):
#     if not user.is_active:
#         raise HTTPException(
#             status_code=400,
#             detail="Your account is inactive. Please contact support.",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     if not user.is_verified:
#         raise HTTPException(
#             status_code=400,
#             detail="Your account is unverified. We have resend the account verification email.",
#             headers={"WWW-Authenticate": "Bearer"},
#         )