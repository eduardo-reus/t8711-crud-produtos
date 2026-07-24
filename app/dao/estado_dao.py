from app.dao.dao import DAO
from app.models.estado import Estado


class Estado_DAO(DAO):

    def __init__(self, database):
        super().__init__(database)

    def save(self, estado):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    INSERT INTO ESTADO
                    (
                        NOME,
                        SIGLA
                    )
                    VALUES
                    (
                        %s,
                        %s
                    )
                  """

            cursor.execute(
                sql,
                (
                    estado.nome,
                    estado.sigla
                )
            )

            conexao.commit()

            estado.id = cursor.lastrowid

            return estado

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def get_all(self):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME,
                        SIGLA
                    FROM
                        ESTADO
                    ORDER BY
                        NOME
                  """

            cursor.execute(sql)

            registros = cursor.fetchall()

            estados = []

            for registro in registros:

                estados.append(

                    Estado(
                        registro[0],
                        registro[1],
                        registro[2]
                    )

                )

            return estados

        finally:
            self.desconectar(cursor, conexao)

    def get_by_id(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    SELECT
                        ID,
                        NOME,
                        SIGLA
                    FROM
                        ESTADO
                    WHERE
                        ID = %s
                  """

            cursor.execute(sql, (id,))

            registro = cursor.fetchone()

            if registro is None:
                return None

            return Estado(
                registro[0],
                registro[1],
                registro[2]
            )

        finally:
            self.desconectar(cursor, conexao)

    def update(self, estado):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    UPDATE ESTADO
                    SET
                        NOME = %s,
                        SIGLA = %s
                    WHERE
                        ID = %s
                  """

            cursor.execute(
                sql,
                (
                    estado.nome,
                    estado.sigla,
                    estado.id
                )
            )

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)

    def delete(self, id):

        conexao, cursor = self.conectar()

        try:

            sql = """
                    DELETE
                    FROM ESTADO
                    WHERE ID = %s
                  """

            cursor.execute(sql, (id,))

            conexao.commit()

            return cursor.rowcount > 0

        except Exception:
            conexao.rollback()
            raise

        finally:
            self.desconectar(cursor, conexao)