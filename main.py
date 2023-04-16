from fastapi import FastAPI
from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from website_example import CustomChatGPT

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request, prompt='Hello'):
    foo = CustomChatGPT(prompt)
    return templates.TemplateResponse("index.html", {"request": request, "myArg": foo})


@app.get("/chatgpt", response_class=JSONResponse)
async def chatGPT(request: Request, prompt: str):
    response = CustomChatGPT(prompt)
    return response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print(CustomChatGPT("HELLO"))
    return {"item_id": item_id, "q": q}


# add API endpoint to call ChatGPT with custom request
# return ChatGPT response


# # Try navigating to "localhost:8000/test-db/world"
# @app.get("/test-db/{word}")
# def test_db(word: str):
#     return query("SELECT %s, %s", ['hello', word])
