from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso
from fastapi import Response
from fastapi import Path
from fastapi import Query
from typing import Optional

app = FastAPI()

cursos = {
    1:{
        'titulo': 'programaçãom pra leigos',
        'aulas':112,
        'horas':58
    },
     2:{
        'titulo': 'programaçãom pra leigos 2',
        'aulas':52,
        'horas':30
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = 
                    #adicionar uma validação  a mais
                    Path(default=None, title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)
                    ):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
    
@app.post('/cursos', status_code= status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
        #gambiara para quando não tem id
        next_id = len(cursos)+1
        cursos[next_id] = curso
        #fazendo isso só pra resposta não ficar null
        del curso.id
        return  curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id:int, curso:Curso):
     if curso_id in cursos:
          cursos[curso_id] = curso
        #fazendo isso só pra resposta não ficar null
          del curso.id
          return curso
     else:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o {curso_id} ')
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id:int):
     if curso_id in cursos:
          del cursos[curso_id]
          #bug no fast api não usar por enquanto
          #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
          return Response(status_code=status.HTTP_204_NO_CONTENT)
          
     else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o {curso_id} ')

@app.get('/calculadora')
async def calcular(a :int =  Query(default= None, gt = 5) ,b : int = Query(default= None, gt = 5),c :Optional[int]= None):
     soma = a+b
     if c:
          soma = soma + c
     return {"Resultado": soma}

               

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)  
