import mysql.connector


class ConexaoBD:

    def __init__(self, host: str, user: str, password: str, db: str) -> object:
        self.conexao = None
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.db = db

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

    

