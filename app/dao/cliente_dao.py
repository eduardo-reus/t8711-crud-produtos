from app.dao.dao import DAO
from app.models.cliente import Cliente
class Cliente_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, cliente):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        INSERT INTO CLIENTE
                        (NOME, DATA_NASCIMENTO, LIMITE_CREDITO)
                        VALUES (%s, %s, %s)
                    """
            cursor.execute(sql, (
                cliente.nome,
                cliente.data_nascimento,
                cliente.limite_credito
            ))
            conexao.commit()
            cliente.id = cursor.lastrowid
            return cliente
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
                            DATA_NASCIMENTO,
                            LIMITE_CREDITO
                        FROM
                            CLIENTE
                        ORDER BY 
                            NOME
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                clientes.append(
                    Cliente(
                        registro[0],
                        registro[1],
                        registro[2],
                        registro[3]
                    )
                )
            return clientes
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
                            DATA_NASCIMENTO,
                            LIMITE_CREDITO
                        FROM
                            CLIENTE
                        WHERE
                            ID = %s
                    """        
            cursor.execute(sql,(id,))
            registro = cursor.fetchone()

            if registro is None:
                return None
            return Cliente(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
            )
        except Exception as e:
            raise e
        finally:
            self.desconectar(cursor, conexao)


    def update(self, cliente):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE CLIENTE SET
                            NOME             = %s,
                            DATA_NASCIMENTO = %s,
                            LIMITE_CREDITO   = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql,(
                                    cliente.nome,
                                    cliente.data_nascimento,
                                    cliente.limite_credito,
                                    cliente.id
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
                        DELETE FROM CLIENTE
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