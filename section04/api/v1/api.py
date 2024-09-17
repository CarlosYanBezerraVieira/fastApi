from api.v1.endpoints import curso
from fastapi import APIRouter

api_router = APIRouter()
# O caminho para esse endpoint é /api/v1/cursos
api_router.include_router(curso.router, prefix="/cursos", tags=["cursos"])
