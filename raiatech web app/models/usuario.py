import re
from typing import List, Optional
from fastapi import Request
from pydantic import BaseModel, Field

from db.conexaoBD import *


class Config:
    host = "bd_rt_teste.mysql.dbaas.com.br"
    user = "bd_rt_teste"
    password = "j1cr.9WCS72021"
    db = "bd_rt_teste"


class Usuario(BaseModel):

    id_email_usuario: str = Field(None, alias="USR_id_email_usuario")
    codigo_tipo_usuario: int = Field(None, alias="TPU_cod_tipo_usuario")
    nome_usuario: str = Field(None, alias="USR_nome_usuario")
    senha_usuario: str = Field(None, alias="USR_nome_usuario")

    def set_usuario(self, id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario):
        self.id_email_usuario = id_email_usuario
        self.codigo_tipo_usuario = codigo_tipo_usuario
        self.nome_usuario = nome_usuario
        self.senha_usuario = senha_usuario

    def inserir(self, id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario):
        self.set_usuario(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"INSERT INTO TB_USR_Usuarios_RT (USR_id_email_usuario, TPU_cod_tipo_usuario, USR_nome_usuario, USR_senha_usuario) "
        sql += f"VALUES ('{id_email_usuario}', {codigo_tipo_usuario}, '{nome_usuario}', '{senha_usuario}')"
        bd.executa_DML(sql)

    def alterar(self, id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario):
        self.set_usuario(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"UPDATE TB_USR_Usuarios_RT "
        sql += f"SET TPU_cod_tipo_usuario = '{codigo_tipo_usuario}' "
        sql += f", USR_nome_usuario = '{nome_usuario}' "
        sql += f", USR_senha_usuario = '{senha_usuario}' "
        sql += f"WHERE USR_id_email_usuario = '{id_email_usuario}'"
        bd.executa_DML(sql)

    def excluir(self, id_email_usuario):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"DELETE FROM TB_USR_Usuarios_RT "
        sql += f"WHERE USR_id_email_usuario = '{id_email_usuario}'"
        bd.executa_DML(sql)

    def consulta(self):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_USR_Usuarios_RT"
        resultado = bd.executa_DQL(sql)
        return resultado

    def consulta_usuario(self, id_email_usuario):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_USR_Usuarios_RT WHERE USR_id_email_usuario = '{id_email_usuario}'"
        resultado = bd.executa_DQL(sql)
        return resultado

    def verifica_login(self, id_email_usuario, senha_usuario):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_USR_Usuarios_RT WHERE USR_id_email_usuario = '{id_email_usuario}' AND USR_senha_usuario = '{senha_usuario}'"
        resultado = bd.executa_DQL(sql)
        try:
            extracao = resultado[0]
            print(extracao[0])

            if id_email_usuario in extracao[0] :
                print("EMAIL ENCONTRADO!")
            if senha_usuario in extracao[2]:
                print("Senha correta!")
                return True
        except:
            return False

    

class login:
    def __init__(self, request:Request):
        self.request: Request = request
        self.erros: List = []
        self.username: Optional[str]= None
        self.password: Optional[str]= None
    async def load_data(self):
        form = await self.request.form()
        self.username = form.get('USR_id_email_usuario')
        self.password = form.get('USR_senha_usuario')
    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.erros.append("Email is not valid")
        if not self.password or not len(self.password)>=4:
            self.erros.append("Senha is not valid")
        if not self.erros:
            return True
        return False