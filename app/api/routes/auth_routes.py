from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)

# @router.post("/token", status_code=status.HTTP_200_OK)
# async def authenticate_user(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     return await get_token(data=data, db=db)