import uvicorn
from fastapi import FastAPI

from usuario import *

app = FastAPI()


@app.get("/")
def raiz():
    return "Raiatech"


@app.get("/usuario")
def get_all_users():
    user = Usuario()
    return user.consulta()


@app.get("/usuario/{id_email_usuario}")
def get_user_by_id(id_email_usuario: str):
    user = Usuario()
    return user.consulta_usuario(id_email_usuario)


@app.post("/usuario")
def set_user(id_email_usuario: str, codigo_tipo_usuario: int, nome_usuario: str, senha_usuario: str):
    user = Usuario()
    user.inserir(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
    return user


@app.put("/usuario/{id_email_usuario}")
def put_user(id_email_usuario: str, codigo_tipo_usuario: int, nome_usuario: str, senha_usuario: str):
    user = Usuario()
    user.alterar(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
    return user


@app.delete("/usuario/{id_email_usuario}")
def delete_user(id_email_usuario: str):
    user = Usuario()
    user.excluir(id_email_usuario)
    return "Ok"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
