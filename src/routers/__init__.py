from fastapi import APIRouter
from routers.users import user_router
from routers.project import project_router

api_router = APIRouter()
api_router.include_router(user_router, prefix= "/auth", tags=["Authentication"])
api_router.include_router(project_router, prefix= "/project", tags=["Project Managment"])