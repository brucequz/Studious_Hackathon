from fastapi import FastAPI
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    foo = 'this is a sentence'
    return templates.TemplateResponse("index.html", {"request": request, "myArg": foo})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# # Try navigating to "localhost:8000/test-db/world"
# @app.get("/test-db/{word}")
# def test_db(word: str):
#     return query("SELECT %s, %s", ['hello', word])
