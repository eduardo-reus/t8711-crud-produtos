class Cliente:
    def __init__(self, id, nome, data_nascimento, limite_credito):
        self._id = id
        self._nome = nome  
        self._data_nascimento = data_nascimento
        self._limite_credito = limite_credito
    
    def atualizar_dados(self, novo_nome, novo_data_nascimento, novo_limite_credito):
        if self._limite_credito < 0:
            raise ValueError("O limite não pode ser negativo.")

        self._nome = novo_nome
        self._data_nascimento = novo_data_nascimento
        self._limite_credito = novo_limite_credito
            
    