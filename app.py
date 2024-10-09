from fastapi import FastAPI
import uvicorn

app =  FASTAPI()

@app.get("/")
def read_root():
    return"Hello Team!"
