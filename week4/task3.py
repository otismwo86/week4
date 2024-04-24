from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
import uvicorn


app = FastAPI()

KEY = "mykey"
SIGNED_IN = "Sign-In"
app.add_middleware(SessionMiddleware, secret_key=KEY)

app.mount("/week4", StaticFiles(directory="task3"))
templates = Jinja2Templates(directory="task3")


user = {
    "username": "test",
    "password": "test"
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    token = request.session.get(SIGNED_IN)
    if token:
        return RedirectResponse(url="/member") 
    return templates.TemplateResponse("task1.html", {'request': request})

@app.post("/signin")
async def sign_in(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == user["username"] and password == user["password"]:
        request.session[SIGNED_IN] = True
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼有誤", status_code=303)


@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    token = request.session.get(SIGNED_IN)
    if not token:
        return RedirectResponse(url="/")
    return templates.TemplateResponse("task2-1.html", {'request': request})

@app.get("/error")
async def error(request:Request, message: str):
    return templates.TemplateResponse(
        "task2-2.html",
        {'request':request,'message': message}
    )

@app.get("/signout")
async def sign_out(request: Request):
    request.session[SIGNED_IN] = False
    return RedirectResponse(url="/")



if __name__ == '__main__':
    uvicorn.run("task3:app", reload=True)