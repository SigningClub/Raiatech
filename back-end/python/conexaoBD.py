import mysql.connector


class ConexaoBD():

    def __init__(self):
        self.host = "bd_rt_teste.mysql.dbaas.com.br"
        self.user = "bd_rt_teste"
        self.password = "j1cr.9WCS72021"
        self.db = "bd_rt_teste"

    def conecta(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db)

        self.cursor = self.conexao.cursor()

    def desconecta(self):
        self.conexao.close()

    def executa_DQL(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.desconecta()
        return resultado

    def executa_DML(self, sql):
        self.conecta()
        self.cursor.execute(sql)
        self.conexao.commit()
        self.desconecta()