from app.api.routes.user_routes import router as user_router
from app.api.routes.auth_routes import router as auth_router
from app.api.routes.main_routes import router as main_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(user_router)
router.include_router(auth_router)
router.include_router(main_router)
