from fastapi import FastAPI
from typing import Union
app = FastAPI()

@app.get("/connect")
def connect_form(name: str, message: str):
    return {"success":"ok"}