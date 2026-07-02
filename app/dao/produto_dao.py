class Produto_DAO:
    def __init__(self):
        self.__produtos = []
        self.__novo_id = 1

    def save(self, produto):
        produto._id = self.__novo_id
        self.__produtos.append(produto)
        self.__novo_id += 1
        return produto
    
    def get_all(self):
        return list(self.__produtos)
    
    def get_by_id(self, id):
        for p in self.__produtos:
            if p._id == id:
                return p
        return None
    
    def delete(self, id):
        produto = self.get_by_id(id)
        if produto:
            self.__produtos.remove(produto)
            return True
        return False
    
    def update(self, produto_atualizado):
        return True