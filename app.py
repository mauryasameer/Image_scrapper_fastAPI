from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return '<h1>YO</h1>'


@app.get('/id/{id}')
async def read_id(id:int,s:str=None):
    return {'id':id,'s':s}
