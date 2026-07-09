class Produto:
    def __init__(self, id, nome, estoque, preco):
        self._id = id
        self._nome = nome  
        self._estoque = estoque
        self._preco = preco

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
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        self._estoque = novo_estoque

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    def atualizar_dados(self, novo_nome, novo_estoque, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        if novo_estoque < 0:
            raise ValueError("O estoque não pode ser negativo.")
        self._nome = novo_nome
        self._estoque = novo_estoque
        self._preco = novo_preco
            

p1 = Produto(1,"Playstation",100,3780)

print(p1.nome)
p1.nome = "Playstation 5 PRO"
