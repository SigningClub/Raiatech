
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/cadastro/")
async def cadastro(nomeUsuario: str = Form(...), email: str = Form(...), senha: str = Form(...), tipo: int = Form(...)):
    db_connection = mysql.connector.connect(host='bd_rt_teste.mysql.dbaas.com.br', user='bd_rt_teste', password='j1cr.9WCS72021', database='bd_rt_teste')
    print("Conexão feita com sucesso!")

    cursor = db_connection.cursor()
    
    sql = """INSERT INTO bd_rt_teste.TB_USR_Usuarios_RT
            (USR_id_email_usuario, USR_nome_usuario, USR_senha_usuario, TPU_cod_tipo_usuario)
            VALUES('{}', '{}', '{}', {});""".format(nomeUsuario,email,senha,tipo)
    cursor.execute(sql)

    cursor.close()
    db_connection.commit()
    db_connection.close()

    return {"nomeUsuario": nomeUsuario, "email": email, "tipo": tipo}


@app.get("/cadastro/get")
async def cadastro():
    db_connection = mysql.connector.connect(host='bd_rt_teste.mysql.dbaas.com.br', user='bd_rt_teste', password='j1cr.9WCS72021', database='bd_rt_teste')
    print("Conexão feita com sucesso!")

    cursor = db_connection.cursor()
    cursor.execute("select * from TB_USR_Usuarios_RT")
    linha = cursor.fetchall()
    
    db_connection.commit()
    db_connection.close()

    return linha


@app.put("/cadastro/put")
async def cadastro(nomeUsuario: str = Form(...), email: str = Form(...), senha: str = Form(...), tipo: int = Form(...)):
    db_connection = mysql.connector.connect(host='bd_rt_teste.mysql.dbaas.com.br', user='bd_rt_teste', password='j1cr.9WCS72021', database='bd_rt_teste')
    print("Conexão feita com sucesso!")

    cursor = db_connection.cursor()
    cursor.execute("""
                    UPDATE TB_USR_Usuarios_RT
                    SET USR_nome_usuario = '{}', USR_senha_usuario = '{}', TPU_cod_tipo_usuario = '{}'
                    WHERE USR_id_email_usuario = '{}';

                    """.format(nomeUsuario,senha,tipo,email))


    db_connection.commit()
    db_connection.close()

    return {"nomeUsuario": nomeUsuario, "email": email, "tipo": tipo}

@app.delete("/cadastro/delete")
async def cadastro(email: str = Form(...)):
    db_connection = mysql.connector.connect(host='bd_rt_teste.mysql.dbaas.com.br', user='bd_rt_teste', password='j1cr.9WCS72021', database='bd_rt_teste')
    print("Conexão feita com sucesso!")

    cursor = db_connection.cursor()
    cursor.execute("""
                    DELETE FROM TB_USR_Usuarios_RT WHERE USR_id_email_usuario='{}';

                    """.format(email))


    db_connection.commit()
    db_connection.close()

    return {"email": email}