import os
from app.models.produto import Produto

class Produto_Controller:
    def __init__(self, dao, fornecedor_dao, view):
        self.dao = dao
        self.fornecedor_dao = fornecedor_dao
        self.view = view
    
    def save(self):
        try:
            fornecedores = self.fornecedor_dao.get_all()
            if not fornecedores:
                self.view.exibir_mensagem("Cadastre fornecedores antes de cadastrar produtos", False)
                return
            self.view.exibir_fornecedores(fornecedores)
            id_fornecedor = self.view.ler_fornecedor()
            fornecedor = self.fornecedor_dao.get_by_id(id_fornecedor)

            if fornecedor is None:
                self.view.exibir_mensagem("Fornecedor não encontrado.", False)
                return

            nome, estoque, preco = self.view.ler_dados_produto()
            produto = Produto(None,nome, estoque, preco, fornecedor)
            self.dao.save(produto)
            self.view.exibir_mensagem("Produto cadastrado com sucesso!")
        except ValueError:
            self.view.exibir_mensagem("Erro: Entrada inválida. Tente novamente.", False)
        except KeyboardInterrupt:
            self.view.exibir_mensagem("Operação cancelada pelo usuário.", False)        
    
    def get_all(self):
        produtos = self.dao.get_all()
        self.view.exibir_produtos(produtos)
        self.view.aguardar_entrada()
    def update(self):
        try:
            produtos = self.dao.get_all()
            self.view.exibir_produtos(produtos)
            id_produto = int(self.view.ler_id())
            produto_existente = self.dao.get_by_id(id_produto)
            if produto_existente:
                fornecedores = self.fornecedor_dao.get_all()
                if not fornecedores:
                    self.view.exibir_mensagem("Cadastre fornecedores antes de cadastrar produtos", False)
                    return
                
                
                self.view.exibir_fornecedores(fornecedores)
                id_fornecedor = self.view.ler_fornecedor(produto_existente.fornecedor.id)
                fornecedor = self.fornecedor_dao.get_by_id(int(id_fornecedor))

                if fornecedor is None:
                    self.view.exibir_mensagem("Fornecedor não encontrado.", False)
                    return                
                nome, estoque, preco = self.view.ler_dados_produto(produto_existente)
                produto_existente.atualizar_dados(nome, estoque, preco, fornecedor)
                self.dao.update(produto_existente)
                self.view.exibir_mensagem("Produto atualizado com sucesso!")
            else:
                self.view.exibir_mensagem("Produto não encontrado.", False) 
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
    
    def delete(self):
        try:
            produtos = self.dao.get_all()
            self.view.exibir_produtos(produtos)
            id_produto = int(self.view.ler_id())
            sucesso = self.dao.delete(id_produto)
            if sucesso:
                self.view.exibir_mensagem("Produto excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Produto não encontrado.", False)
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
                
