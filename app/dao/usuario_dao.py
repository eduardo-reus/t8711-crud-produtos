from app.dao.dao import DAO
from app.models.usuario import Usuario
class Usuario_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, usuario):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        INSERT INTO USUARIO
                        (NOME, EMAIL, DATA_NASCIMENTO)
                        VALUES (%s, %s, %s)
                    """
            cursor.execute(sql, (
                usuario.nome,
                usuario.email,
                usuario.data_nascimento
            ))
            conexao.commit()
            usuario.id = cursor.lastrowid
            return usuario
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
    
    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        SELECT
                            ID,
                            NOME,
                            EMAIL,
                            DATA_NASCIMENTO
                        FROM
                            USUARIO
                        ORDER BY 
                            NOME
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuarios.append(
                    Usuario(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3]
                    )
                )
            return usuarios
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)
    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        SELECT
                            ID,
                            NOME,
                            EMAIL,
                            DATA_NASCIMENTO
                        FROM
                            USUARIO
                        WHERE
                            ID = %s
                    """        
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Usuario(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
            )
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)

    def update(self, usuario):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE USUARIO SET
                            NOME            = %s,
                            EMAIL           = %s,
                            DATA_NASCIMENTO = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql,(
                                    usuario.nome,
                                    usuario.email,
                                    usuario.data_nascimento,
                                    usuario.id
            ))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)
        
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                    DELETE FROM USUARIO
                    WHERE ID = %s
                """
            cursor.execute(sql,(id,))
            conexao.commit()
            sucesso = cursor.rowcount > 0
            return sucesso
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            self.desconectar(cursor, conexao)