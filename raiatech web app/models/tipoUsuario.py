from pydantic import BaseModel, Field

from db.conexaoBD import *


class Config:
    host = "bd_rt_teste.mysql.dbaas.com.br"
    user = "bd_rt_teste"
    password = "j1cr.9WCS72021"
    db = "bd_rt_teste"


class TipoUsuario(BaseModel):

    id_tipo_user: str = Field(None, alias="TPU_cod_tipo_usuario")
    descricao_tipo_usuario: int = Field(None, alias="TPU_descricao_tipo_usuario")

    def set_tipo_user(self, id_tipo_user, descricao_tipo_usuario):
        self.id_tipo_user = id_tipo_user
        self.descricao_tipo_usuario = descricao_tipo_usuario


    def consulta_todos(self):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_TPU_Tipo_Usuario_RT"
        resultado = bd.executa_DQL(sql)
        return resultado

    def consulta_tipo_usuario(self, id_tipo_user):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_TPU_Tipo_Usuario_RT WHERE TPU_cod_tipo_usuario = '{id_tipo_user}'"
        resultado = bd.executa_DQL(sql)
        return resultado    

    def inserir(self, id_tipo_user, descricao_tipo_usuario):
        self.set_tipo_user(id_tipo_user, descricao_tipo_usuario)
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"INSERT INTO TB_TPU_Tipo_Usuario_RT (TPU_cod_tipo_usuario, TPU_descricao_tipo_usuario) "
        sql += f"VALUES ('{id_tipo_user}', '{descricao_tipo_usuario}')"
        bd.executa_DML(sql)

    def alterar(self, id_tipo_user, descricao_tipo_usuario):
        self.set_tipo_user(id_tipo_user, descricao_tipo_usuario)
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"UPDATE TB_TPU_Tipo_Usuario_RT "
        sql += f"SET TPU_descricao_tipo_usuario = '{descricao_tipo_usuario}' "
        sql += f"WHERE TPU_cod_tipo_usuario = '{id_tipo_user}'"
        bd.executa_DML(sql)

    def excluir(self, id_tipo_user):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"DELETE FROM TB_TPU_Tipo_Usuario_RT WHERE TPU_cod_tipo_usuario = '{id_tipo_user}'"
        bd.executa_DML(sql)

    
