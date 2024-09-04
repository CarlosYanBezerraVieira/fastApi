from time import sleep
from typing import Any, Dict, List, Optional

from fastapi import (
    Depends,
    FastAPI,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    status,
)
from models import Curso, cursos


def fake_db():
    try:
        print("Abrindo conexão com banco de dados...")
        sleep(1)
    finally:
        print("Fechando conexão com banco de dados...")
        sleep(1)


# configuração da documentação
app = FastAPI(
    title="Api de estudo",
    version="0.0.1",
    description="Uma api para estudo do FastApi",
)


@app.get(
    "/cursos",
    # informações do endpoint na doc
    description="Retorna todos os cursos ou uma lista vazia",
    summary="Retorna todos os cursos",
    response_model=List[Curso],
    response_description="Cursos encontrados com sucesso",
)
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(
    curso_id: int =
    # adicionar uma validação  a mais
    Path(
        default=None,
        title="ID do curso",
        description="Deve ser entre 1 e 2",
        gt=0,
        lt=3,
    ),
    db: Any = Depends(fake_db),
):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado"
        )


@app.post("/cursos", status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    # gambiara para quando não tem id
    next_id = len(cursos) + 1
    curso.id = next_id
    cursos.insert(next_id, curso)
    return curso


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if len(list(filter(lambda x: x.id == curso_id, cursos))) != 0:
        curso.id = curso_id
        cursos[curso_id - 1] = curso
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não existe curso com o {curso_id} ",
        )


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if len(list(filter(lambda x: x.id == curso_id, cursos))) != 0:
        del cursos[curso_id - 1]
        # bug no fast api não usar por enquanto
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não existe curso com o {curso_id} ",
        )


@app.get("/calculadora")
async def calcular(
    a: int = Query(default=None, gt=5),
    b: int = Query(default=None, gt=5),
    # dados que vem do header geralmente se usa prefixo x
    x_geek: str = Header(
        default=None,
    ),
    c: Optional[int] = None,
):
    soma = a + b
    if c:
        soma = soma + c
    print(f"X-GEEK: {x_geek}")
    return {"Resultado": soma}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
