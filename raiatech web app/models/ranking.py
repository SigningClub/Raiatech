from pydantic import BaseModel, Field

from db.conexaoBD import *


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

    def set_ranking(self, id_email_usuario, pontuacao, nivel, coins, trofeus, medalhas):
        self.id_email_usuario = id_email_usuario
        self.pontuacao = pontuacao
        self.nivel = nivel
        self.coins = coins
        self.trofeus = trofeus
        self.medalhas = medalhas

    def consulta(self):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_RAU_Ranking_Usuario_RT"
        resultado = bd.executa_DQL(sql)
        return resultado

    def consulta_usuario(self, id_email_usuario):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_RAU_Ranking_Usuario_RT WHERE USR_id_email_usuario = '{id_email_usuario}'"
        resultado = bd.executa_DQL(sql)
        return resultado
