from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/login_user")
async def login_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}

@router.get("/get_user")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}
