from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/auth")
async def login():
    return {"message": "Login successful"}
