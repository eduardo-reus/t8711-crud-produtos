from app.dao.dao import DAO
from app.models.cliente import Cliente
class Cliente_DAO(DAO):
    def __init__(self, database):
        self._database = database

    def save(self, cliente):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
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
        self._database.desconectar(cursor, conexao)
        return cliente
    
    def get_all(self):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
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
        self._database.desconectar(cursor, conexao)
        return clientes
    
    def get_by_id(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
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
        self._database.desconectar(cursor, conexao)
        if registro is None:
            return None
        return Cliente(
            registro[0],
            registro[1],
            registro[2],
            registro[3]
        )


    def update(self, cliente):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
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
        self._database.desconectar(cursor, conexao)
        return sucesso
    
    def delete(self, id):
        conexao = self._database.conectar()
        cursor = conexao.cursor()
        sql =   """
                    DELETE FROM CLIENTE
                    WHERE ID = %s
                """
        cursor.execute(sql,(id,))
        conexao.commit()
        sucesso = cursor.rowcount > 0
        self._database.desconectar(cursor, conexao)
        return sucesso