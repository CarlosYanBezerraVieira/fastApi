from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso

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
async def get_curso(curso_id: int):
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


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)  
