from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()

# app.mount("/kmj", StaticFiles(directory="dir_html"), name="my_item") # 이건 태스트 용 인거 같다

templates = Jinja2Templates(directory="dir_html")# dir_html 폴더를 선택한다.

@app.get("/", response_class=HTMLResponse)#get 방식에 / 의 요청을 받는다
async def read_item(request: Request):
    return templates.TemplateResponse("my_item.html", {"request": request}) #templates에 정의된 폴더에서 my_item.html 파일을 찿아 / 경로에 홈패이지를 출력 한다

@app.post("/")#post 방식의 요청을 받는다
async def create_item(username: str = Form(...), password: str = Form(...)): # Form(...) 함수는 HTML 양식의 name 속성을 사용하여 데이터를 추출
    print(f'{username}_{password}')
    return {"username": username, "password": password} # json 타입으로 보낼 수 있다




# uvicorn main:app 명령은 다음을 의미한다:
# main: 파일 main.py (파이썬 모듈) ex) 파일 이름이 kkkk면 uvicorn kkkk:(안의 바인드 이름)
# app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트. ex) aaaa = FastAPI() 면 uvicorn (파일 이름):aaaa 로
# --reload: 코드 변경 후 서버 재시작. 개발에만 사용.
# 실행할 파일의 폴더에서 실행 해야 한다
# 옵션도 있다 uvicorn main:app --port XXXX(번호) --reload (파일이 변경될경우 재시작)