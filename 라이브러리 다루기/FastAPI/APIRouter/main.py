from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="dir_html")

@router.get('/hello', response_class=HTMLResponse)
async def say_hello(request: Request) -> dict:
    return templates.TemplateResponse("my_item.html", {"request": request})

@router.post('/')
async def create_item(username: str = Form(...), password: str = Form(...)): # Form(...) 함수는 HTML 양식의 name 속성을 사용하여 데이터를 추출
    print(f'{username}_{password}')
    return {"username": username, "password": password} # json 타입으로 보낼 수 있다

