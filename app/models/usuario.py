class Usuario:
    def __init__(self, id, nome, email, data_nascimento):
        self._id = id
        self._nome = nome  
        self._email = email
        self._data_nascimento = data_nascimento
    
    def atualizar_dados(self, novo_nome, novo_email, novo_data_nascimento):
        self._nome = novo_nome
        self._email = novo_email
        self._data_nascimento = novo_data_nascimento
            
    