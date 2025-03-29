from fastapi import APIRouter

router = APIRouter(prefix="", tags=["main"])

@router.get("/")
def main():
    return {"message": "FastAPI"}
