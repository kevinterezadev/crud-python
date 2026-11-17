import database as db


class Estado:
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.sigla = ""
        self.db = db.ConexaoMySQL()

    def salvar(self):
        conn = self.db.abrir()
        if conn is None:
            return False
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO estado (nome, sigla) VALUES (%s, %s)",
                    (self.nome, self.sigla),
                )
                conn.commit()
                self.id = cursor.lastrowid
            print("Salvo com sucesso!")
            return True
        except Exception as erro:
            conn.rollback()
            print(f"Erro ao salvar estado: {erro}")
            return False
        finally:
            self.db.fechar()

    def listar(self):
        conn = self.db.abrir()
        if conn is None:
            return []
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nome, sigla FROM estado ORDER BY id")
                return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar estados: {erro}")
            return []
        finally:
            self.db.fechar()

    def atualizar(self):
        conn = self.db.abrir()
        if conn is None:
            return False
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE estado SET nome = %s, sigla = %s WHERE id = %s",
                    (self.nome, self.sigla, self.id),
                )
                conn.commit()
                alterado = cursor.rowcount > 0
            print("Atualizado com sucesso!" if alterado else "Nenhum estado encontrado com esse ID.")
            return alterado
        except Exception as erro:
            conn.rollback()
            print(f"Erro ao atualizar estado: {erro}")
            return False
        finally:
            self.db.fechar()

    def excluir(self):
        conn = self.db.abrir()
        if conn is None:
            return False
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM estado WHERE id = %s", (self.id,))
                conn.commit()
                excluido = cursor.rowcount > 0
            print("Excluído com sucesso!" if excluido else "Nenhum estado encontrado com esse ID.")
            return excluido
        except Exception as erro:
            conn.rollback()
            print(f"Erro ao excluir estado: {erro}")
            return False
        finally:
            self.db.fechar()
