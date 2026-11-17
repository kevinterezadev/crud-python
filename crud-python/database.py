import os

import pymysql


class ConexaoMySQL:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "endereco")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.conexao = None

    def abrir(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                cursorclass=pymysql.cursors.DictCursor,
                charset="utf8mb4",
            )
            return self.conexao
        except pymysql.MySQLError as erro:
            print(f"Erro ao conectar ao MySQL: {erro}")
            self.conexao = None
            return None

    def fechar(self):
        if self.conexao and self.conexao.open:
            self.conexao.close()
        self.conexao = None
