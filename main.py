from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    file_path = os.path.join(os.path.dirname(__file__), "main.html")
    with open(file_path, "r") as file:
        content = file.read()
    return HTMLResponse(content=content, status_code=200)

@app.get("/book")
def read_about():
    file_path = os.path.join(os.path.dirname(__file__), "page2.html")
    with open(file_path, "r") as file:
        content = file.read()
    return HTMLResponse(content=content, status_code=200)

@app.get("/reserve")
def read_reserve():
    file_path = os.path.join(os.path.dirname(__file__), "page3.html")
    with open(file_path, "r") as file:
        content = file.read()
    return HTMLResponse(content=content, status_code=200)
