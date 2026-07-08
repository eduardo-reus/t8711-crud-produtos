import os
from app.models.cliente import Cliente

class Cliente_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
    
    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                break
            elif opcao == 1:
                try:
                    nome, data_nascimento, limite_credito = self.view.ler_dados_cliente()
                    cliente = Cliente(None,nome, data_nascimento, limite_credito)
                    self.dao.save(cliente)
                    self.view.exibir_mensagem("Cliente cadastrado com sucesso!")
                except ValueError:
                    self.view.exibir_mensagem("Erro: Entrada inválida. Tente novamente.", False)
                except KeyboardInterrupt:
                    self.view.exibir_mensagem("Operação cancelada pelo usuário.", False)
                
            
            elif opcao == 2:
                clientes = self.dao.get_all()
                self.view.exibir_clientes(clientes)
                self.view.aguardar_entrada()
            
            elif opcao == 3:
                try:
                    clientes = self.dao.get_all()
                    self.view.exibir_clientes(clientes)
                    id_cliente = int(self.view.ler_id())
                    cliente_existente = self.dao.get_by_id(id_cliente)
                    if cliente_existente:
                        nome, data_nascimento, limite_credito = self.view.ler_dados_cliente()
                        cliente_existente.atualizar_dados(nome, data_nascimento, limite_credito)
                        self.dao.update(cliente_existente)
                        self.view.exibir_mensagem("Cliente atualizado com sucesso!")
                    else:
                        self.view.exibir_mensagem("Cliente não encontrado.", False) 
                except ValueError as e:
                    self.view.exibir_mensagem(f"Erro: {str(e)}", False)
                
            
            elif opcao == 4:
                try:
                    clientes = self.dao.get_all()
                    self.view.exibir_clientes(clientes)
                    id_cliente = int(self.view.ler_id())
                    sucesso = self.dao.delete(id_cliente)
                    if sucesso:
                        self.view.exibir_mensagem("Cliente excluído com sucesso!")
                    else:
                        self.view.exibir_mensagem("Cliente não encontrado.", False)
                except ValueError:
                    self.view.exibir_mensagem("Erro: ID inválido", False)
                
            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.", False)
                
