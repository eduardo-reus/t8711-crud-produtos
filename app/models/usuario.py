class Usuario:
    def __init__(self, id, nome, email, data_nascimento):
        self._id = id
        self._nome = nome  
        self._email = email
        self._data_nascimento = data_nascimento
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    # Encapsulamento do Nome
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    # Encapsulamento do Email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    # Encapsulamento da Data de Nascimento
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        self._data_nascimento = nova_data  
          
    def atualizar_dados(self, novo_nome, novo_email, novo_data_nascimento):
        self._nome = novo_nome
        self._email = novo_email
        self._data_nascimento = novo_data_nascimento
            
    