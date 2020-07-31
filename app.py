from fastapi import FastAPI, requests
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static',StaticFiles(directory='static'),name = 'static' )
@app.get('/')
def root(request: Request):
    return templates.TemplateResponse('index.html',{'request':request})

@app.get('/id/{id}')
async def read_id(id:int,s:str=None):
    return {'id':id,'s':s}