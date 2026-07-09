from abc import ABC, abstractmethod
class DAO(ABC):
    @abstractmethod
    def save(self, objeto):
        pass

    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def update(self, objeto):
        pass

    @abstractmethod
    def delete(self, id):
        pass