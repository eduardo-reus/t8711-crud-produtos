from app.core.data_utils import Data_Utils
class Cliente:
    def __init__(self, id, nome, data_nascimento, limite_credito):
        self._id = id
        self._nome = nome  
        self._data_nascimento = data_nascimento
        self._limite_credito = limite_credito
    
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, novo_data_nascimento):
        self._data_nascimento = novo_data_nascimento

    @property
    def limite_credito(self):
        return self._limite_credito

    @limite_credito.setter
    def limite_credito(self, novo_limite_credito):
        self._limite_credito = novo_limite_credito
    
    @property
    def idade(self):
        return Data_Utils.calcular_idade(self._data_nascimento)

    def atualizar_dados(self, novo_nome, novo_data_nascimento, novo_limite_credito):
        if novo_limite_credito < 0:
            raise ValueError("O limite não pode ser negativo.")

        self._nome = novo_nome
        self._data_nascimento = novo_data_nascimento
        self._limite_credito = novo_limite_credito
            
    