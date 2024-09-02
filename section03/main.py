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


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)  
