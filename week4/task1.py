from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
import uvicorn


app = FastAPI()
app.mount("/week4", StaticFiles(directory="task1"))
templates=Jinja2Templates(directory="task1")

@app.get('/',response_class=HTMLResponse)
async def index(request:Request):
    return templates.TemplateResponse(
        "task1.html"
        ,{'request':request,"id":id})


if __name__=='__main__':
    uvicorn.run("task1:app",reload=True)