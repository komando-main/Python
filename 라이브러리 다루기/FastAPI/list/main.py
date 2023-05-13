from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/list", StaticFiles(directory="CSS"), name="CSS1")
app.mount("/sss1", StaticFiles(directory="qwe"), name="list")
t = Jinja2Templates(directory="html")

list = ['안녕하세요', '반갑습니다', '고맙습니다', '좋은하루내요', '즐거운 하루되세요']

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return t.TemplateResponse("list.html", {"request": request, "list": list})