from fastapi import FastAPI, Request as res
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
from crawler_utils import crawler
import os

app = FastAPI()



templates = Jinja2Templates(directory='templates')
app.mount('/static',StaticFiles(directory='static'),name = 'static' )


def list_only_jpg_files(folder_name):

    list_of_jpg_files=[]
    list_of_files=os.listdir(folder_name)
    print('list of files==')
    print(list_of_files)
    for file in list_of_files:
        name_array= file.split('.')
        if(name_array[1]=='jpg'):
            list_of_jpg_files.append(folder_name+'/'+file)
        else:
            print('filename does not end withn jpg')
    return list_of_jpg_files


@app.get('/')
def root(request: Request):
    return templates.TemplateResponse('index.html',{'request':request})

# @app.get('/id/{id}')
# async def read_id(id:int,s:str=None):
#     return {'id':id,'s':s}

@app.post('/searchImages')
async def searchImages(req:res):
    data=await req.form()
    crw = crawler()
    crw.search_and_download(data['keyword'])
    output_location = crw.TARGET_LOCATION+f"/{data['keyword']}"
    im_list=list_only_jpg_files(output_location)
    return templates.TemplateResponse('showimage.html',{
            'request':req,
            'user_images':im_list,
    })