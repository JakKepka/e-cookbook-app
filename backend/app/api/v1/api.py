from fastapi import APIRouter
from app.api.v1.endpoints import expert

api_router = APIRouter()

api_router.include_router(expert.router, prefix="/expert", tags=["expert"]) 