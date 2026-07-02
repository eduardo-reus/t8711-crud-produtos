import os
from app.dao.produto_dao import Produto_DAO
from app.views.produto_view import Produto_Terminal_View
from app.controllers.produto_controller import Produto_Controller

if __name__ == "__main__":
    dao = Produto_DAO()
    view = Produto_Terminal_View()
    controller = Produto_Controller(dao, view)
    controller.inicializar_sistema()