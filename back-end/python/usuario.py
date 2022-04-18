from conexaoBD import *


class Usuario():

    def __init__(self, id_email_usuario=None, codigo_tipo_usuario=None, nome_usuario=None, senha_usuario=None):
        self.id_email_usuario = id_email_usuario
        self.codigo_tipo_usuario = codigo_tipo_usuario
        self.nome_usuario = nome_usuario
        self.senha_usuario = senha_usuario

    def inserir(self):
        bd = ConexaoBD()
        sql = f"INSERT INTO TB_USR_Usuarios_RT (USR_id_email_usuario, TPU_codigo_tipo_usuario, USR_nome_usuario, USR_senha_usuario) "
        sql += f"VALUES ('{self.id_email_usuario}', {self.codigo_tipo_usuario}, '{self.nome_usuario}', '{self.senha_usuario}')"
        bd.executa_DML(sql)

    def alterar(self, id_email_usuario, nome_usuario, senha_usuario):
        bd = ConexaoBD()
        sql = f"UPDATE TB_USR_Usuarios_RT "
        sql += f"SET USR_nome_usuario = '{nome_usuario}' "
        sql += f"SET USR_senha_usuario = '{senha_usuario}' "
        sql += f"WHERE USR_id_email_usuario = {id_email_usuario}"
        bd.executa_DML(sql)

    def excluir(self, id_email_usuario):
        bd = ConexaoBD()
        sql = f"DELETE FROM TB_USR_Usuarios_RT "
        sql += f"WHERE USR_id_email_usuario = {id_email_usuario}"
        bd.executa_DML(sql)

    def consulta(self):
        bd = ConexaoBD()
        sql = f"SELECT * FROM TB_USR_Usuarios_RT"
        resultado = bd.executa_DQL(sql)
        return resultado

    def consulta_usuario(self, id_email_usuario):
        bd = ConexaoBD()
        sql = f"SELECT * FROM TB_USR_Usuarios_RT WHERE WHERE USR_id_email_usuario = {id_email_usuario}"
        resultado = bd.executa_DQL(sql)
        return resultado
