class Usuario_DAO:
    def __init__(self):
        self.__usuarios = []
        self.__novo_id = 1

    def save(self, usuario):
        usuario._id = self.__novo_id
        self.__usuarios.append(usuario)
        self.__novo_id += 1
        return usuario
    
    def get_all(self):
        return list(self.__usuarios)
    
    def get_by_id(self, id):
        for u in self.__usuarios:
            if u._id == id:
                return u
        return None
    
    def delete(self, id):
        usuario = self.get_by_id(id)
        if usuario:
            self.__usuarios.remove(usuario)
            return True
        return False
    
    def update(self, usuario_atualizado):
        return True