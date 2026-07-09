from app.dao.dao import DAO
class Generic_DAO(DAO):

    def __init__(self):
        self._dados = []
        self._novo_id = 1

    def save(self, objeto):
        objeto._id = self._novo_id
        self._dados.append(objeto)
        self._novo_id += 1
        return objeto

    def get_all(self):
        return list(self._dados)

    def get_by_id(self, id):

        for objeto in self._dados:
            if objeto._id == id:
                return objeto

        return None

    def delete(self, id):

        objeto = self.get_by_id(id)

        if objeto:
            self._dados.remove(objeto)
            return True

        return False

    def update(self, objeto):
        return True
