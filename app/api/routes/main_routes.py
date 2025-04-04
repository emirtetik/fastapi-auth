from fastapi import APIRouter

router = APIRouter(prefix="", tags=["Main"])

@router.get("/")
def main():
    return {"message": "FastAPI"}
