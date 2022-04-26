from pydantic import BaseModel, Field, validator

from db.conexaoBD import *
from . import usuario


class Config:
    host = "bd_rt_teste.mysql.dbaas.com.br"
    user = "bd_rt_teste"
    password = "j1cr.9WCS72021"
    db = "bd_rt_teste"

class Ranking(BaseModel):

    id_email_usuario: str = Field(None, alias="USR_id_email_usuario")
    pontuacao: int = Field(None, alias="RAU_pontuacao_usuario")
    nivel: int = Field(None, alias="RAU_nivel_usuario")
    coins: int = Field(None, alias="RAU_coins_usuario")
    trofeus: int = Field(None, alias="RAU_trofeus_usuario")
    medalhas: int = Field(None, alias="RAU_medalhas_usuario")

    @validator('id_email_usuario')
    def verificar_usuario(cls, id_email_usuario: str):
        existe = False
        user = Usuario().consulta_usuario(id_email_usuario)
        print(user)
        if user:
            existe = True
        return existe

    def set_ranking(self, id_email_usuario, pontuacao, nivel, coins, trofeus, medalhas):
        self.id_email_usuario = id_email_usuario
        self.pontuacao = pontuacao
        self.nivel = nivel
        self.coins = coins
        self.trofeus = trofeus
        self.medalhas = medalhas

    def consulta_ranking(self):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_RAU_Ranking_Usuario_RT"
        resultado = bd.executa_DQL(sql)
        return resultado

    def consulta_ranking_usuario(self, id_email_usuario):
        if self.verificar_usuario(id_email_usuario):
            bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
            sql = f"SELECT * FROM TB_RAU_Ranking_Usuario_RT WHERE USR_id_email_usuario = '{id_email_usuario}'"
            resultado = bd.executa_DQL(sql)
            return resultado
        else:
            return "Usuário não cadastrado!"
