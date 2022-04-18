import uvicorn
from fastapi import FastAPI

from usuario import *

app = FastAPI()

@app.get("/")
def raiz():
    return "Raiatech"

@app.get("/usuarios")
def get_all_users():
    user = Usuario()
    return user.consulta()

@app.get("/usuario/{id_email_usuario}")
def get_user_by_id(id_email_usuario: str):
    user = Usuario()
    return user.consulta_usuario(id_email_usuario)

@app.post("/usuario")
def set_user(usuario: Usuario):
    user = Usuario(usuario)
    user.inserir()
    return user

@app.put("usuario/{id_email_usuario}")
def put_user(id_email_usuario: str, usuario: Usuario):
    user = Usuario()
    user.alterar(usuario.id_email_usuario, usuario.nome_usuario, usuario.senha_usuario)
    return user

@app.delete("usuario/{id_email_usuario}")
def delete_user(id_email_usuario: str, usuario: Usuario):
    user = Usuario()
    user.excluir(usuario.id_email_usuario)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
