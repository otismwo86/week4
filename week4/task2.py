from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse,FileResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
app.mount("/week4", StaticFiles(directory="task2"))
templates=Jinja2Templates(directory="task2")
test_username = "test"
test_password = "test"

class User_Info(BaseModel):
    username:str
    password:str

@app.get('/',response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse(
        "task1.html"
        ,{'request':request})

@app.post("/signin")
async def sign_in(request: Request,username: str = Form(), password: str = Form()):
    form = await request.form()
    username = form.get('username')
    password = form.get('password')
    if username == test_username and password == test_password:
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼有誤", status_code=303)
    

@app.get("/member")
async def member(request:Request):
    return templates.TemplateResponse(
        "task2-1.html"
        ,{'request':request})


@app.get("/error")
async def error(request:Request, message: str):
    return templates.TemplateResponse(
        "task2-2.html",
        {'request':request,'message': message}
    )

if __name__=='__main__':
    uvicorn.run("task2:app",reload=True)