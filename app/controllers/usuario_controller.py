import os
from app.models.usuario import Usuario
from app.core.data_utils import Data_Utils

class Usuario_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
    def save(self):
        try:
            nome, email, data_nascimento = self.view.ler_dados_usuario()
            usuario = Usuario(None,nome, email, Data_Utils.string_para_data(data_nascimento))
            self.dao.save(usuario)
            self.view.exibir_mensagem("Usuário cadastrado com sucesso!")
        except ValueError:
            self.view.exibir_mensagem("Erro: Entrada inválida. Tente novamente.", False)
        except KeyboardInterrupt:
            self.view.exibir_mensagem("Operação cancelada pelo usuário.", False)

    def get_all(self):
        usuarios = self.dao.get_all()
        self.view.exibir_usuarios(usuarios)
        self.view.aguardar_entrada()
    def update(self):
        try:
            usuarios = self.dao.get_all()
            self.view.exibir_usuarios(usuarios)
            id_usuario = int(self.view.ler_id())
            usuario_existente = self.dao.get_by_id(id_usuario)
            if usuario_existente:
                nome, email, data_nascimento = self.view.ler_dados_usuario(usuario_existente)
                usuario_existente.atualizar_dados(nome, email, Data_Utils.string_para_data(data_nascimento))
                self.dao.update(usuario_existente)
                self.view.exibir_mensagem("Usuário atualizado com sucesso!")
            else:
                self.view.exibir_mensagem("Usuário não encontrado.", False) 
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
    def delete(self):
        try:
            usuarios = self.dao.get_all()
            self.view.exibir_usuarios(usuarios)
            id_usuario = int(self.view.ler_id())
            sucesso = self.dao.delete(id_usuario)
            if sucesso:
                self.view.exibir_mensagem("Usuário excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Usuário não encontrado.", False)
        except ValueError:
            self.view.exibir_mensagem("Erro: ID inválido", False)

    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                break
            elif opcao == 1:
                self.save()
            
            elif opcao == 2:
                self.get_all()
            
            elif opcao == 3:
                self.update()
                
            
            elif opcao == 4:
                self.delete()
                
            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.", False)
                
