import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models.usuario import *
from models.tipoUsuario import *
from models.ranking import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
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

@app.get("/tipousuario")
def get_all_tipo_usuario():
    tipo = TipoUsuario()
    return tipo.consulta_todos()


@app.get("/tipousuario/{id_tipo_user}")
def get_tipo_by_id(id_tipo_user: str):
    tipo = TipoUsuario()
    return tipo.consulta_tipo_usuario(id_tipo_user)


@app.post("/tipousuario")
def set_tipo_usuario(id_tipo_user: str, descricao_tipo_usuario: str):
    tipo = TipoUsuario()
    tipo.inserir(id_tipo_user,descricao_tipo_usuario)
    return tipo


@app.put("/tipousuario/{id_tipo_user}")
def put_tipo_user(id_tipo_user: str, descricao_tipo_usuario: str):
    tipo = TipoUsuario()
    tipo.alterar(id_tipo_user, descricao_tipo_usuario)
    return tipo


@app.delete("/tipousuario/{id_tipo_user}")
def delete_tipo_user(id_tipo_user: str):
    tipo = TipoUsuario()
    tipo.excluir(id_tipo_user)
    return "Deletado com sucesso"

@app.get("/ranking")
def get_ranking():
    ranking = Ranking()
    return ranking.consulta_ranking()

@app.get("/ranking/{id_email_usuario}")
def get_ranking_by_id(id_email_usuario: str):
    ranking = Ranking()
    return ranking.consulta_ranking_usuario(id_email_usuario)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
