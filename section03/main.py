from fastapi import FastAPI

app = FastAPI()

cursos = {
    1:{
        'itulo': 'programaçãom pra leigos',
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
    curso = cursos[curso_id]
    curso.update({'id': curso_id})
    return curso

 

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)  
