from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    # deve seguir esse padrão de parametros
    @validator("titulo")
    def validar_titulo(cls, value: str):
        palavras = value.split(" ")
        # validações
        if len(palavras) < 3:
            raise ValueError("O titulo deve ter pelo menos 3 palavras")
        if value.islower():
            raise ValueError("O titulo deve ser capitalizado")
        return value


cursos = [
    Curso(id=1, titulo="Programação Para Leigos", aulas=112, horas=58),
    Curso(id=2, titulo="Programação Para Leigos 2", aulas=59, horas=30),
]
