from fastapi import FastAPI, Request as res
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from crawler_utils import search_and_download

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount('/static',StaticFiles(directory='static'),name = 'static' )
@app.get('/')
def root(request: Request):
    return templates.TemplateResponse('index.html',{'request':request})

@app.get('/id/{id}')
async def read_id(id:int,s:str=None):
    return {'id':id,'s':s}

@app.post('/searchImages')
async def searchImages(req:res):
    data=await req.form()
    print(data['keyword'])
    return {'val':1}