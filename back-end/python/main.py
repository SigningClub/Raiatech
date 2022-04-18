import uvicorn
from fastapi import FastAPI

from usuario import *

app = FastAPI()

@app.get("/")
async def read_root():
    user = Usuario()
    return user.consulta()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
