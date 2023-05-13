from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/stylesheet", StaticFiles(directory="test_CSS"), name="test_CSS")
app.mount("/mount_path",StaticFiles(directory="test_dir_js"), name="test_js")#별거 아닌거에 시간 죽어라 뺏겻다 /mount_path 는 웹에서 접근할때의 경로 http://localhost:8000/**mount_path**/test.js 이런싞으로
templ=Jinja2Templates(directory="test_html")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templ.TemplateResponse("test.html", {"request":request})