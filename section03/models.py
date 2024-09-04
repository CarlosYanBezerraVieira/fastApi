from typing import Optional

from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo="programaçãom pra leigos", aulas=112, horas=58),
    Curso(id=2, titulo="programaçãom pra leigos2", aulas=59, horas=30),
]
