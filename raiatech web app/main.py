import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi_login import LoginManager
from fastapi.middleware.cors import CORSMiddleware


from models.usuario import *
from models.tipoUsuario import *
from models.ranking import *

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET = 'G@LATIKA!MAT' 
app.mount("/static", StaticFiles(directory="static"), name="static")
manager = LoginManager(SECRET, token_url='/auth/token')
templates = Jinja2Templates(directory="templates")

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def load_user(id_email_usuario: str):
    return get_user_by_id(id_email_usuario)

@app.post("/login")
def logar(user: Usuario):
    email = user.id_email_usuario
    senha = user.senha_usuario

    set_user = Usuario.find_password(email)
    user = load_user(email)
    
    if not user:
        return {'error': 'User or Password invalid'}

    if set_user[0][0] != senha:
        return {'error': 'User or Password invalid'}

    access_token = manager.create_access_token(
        data=dict(sub=email)
    )

    return {'access_token': access_token, 'token_type': 'bearer'}

@app.get("/usuario")
def get_all_users():
    user = Usuario()
    return user.consulta()

@app.get("/usuario/{id_email_usuario}")
def get_user_by_id(id_email_usuario: str):
    user = Usuario()
    return user.consulta_usuario(id_email_usuario)


@app.post("/usuario")
def set_user(user: Usuario):
    user.inserir(user.id_email_usuario, user.codigo_tipo_usuario, user.nome_usuario, user.senha_usuario)
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
