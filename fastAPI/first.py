from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from typing import List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/')
def home():
    return {"message": "first api"}

@app.get('/{id}')
def user_name(id : int = Path(..., max_length=5, min_length=3), name =None, city= None):
    return {'id': id, "name":name, 'city': city}

class Student(BaseModel):
    stu_id : int
    stu_name : str
    stu_address: str

@app.get('/student/{stid}')
def student_info(stid, name, address):
    data = {
        'stu_id' : stid,
        'stu_name' : name,
        'stu_address' : address
    }
    print(type(stid))
    s1 = Student(**data)
    print(type(s1.stu_id))

@app.post('/stu')
def ispost(s1: Student):
    return s1

@app.get('/hello/', response_class=HTMLResponse)
async def hello(request: Request):
    name = 'ravina'
    return templates.TemplateResponse('hello.html', {"request": request, 'context':name })