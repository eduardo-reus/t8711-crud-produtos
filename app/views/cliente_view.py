from colorama import init, Fore, Style
from app.core.data_utils import Data_Utils

init(autoreset=True)

class Cliente_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE CLIENTES (MVC) ==="
    
    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar cliente")
        print(f"2 - Listar clientes")
        print(f"3 - Atualizar cliente")
        print(f"4 - Excluir cliente")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
    def ler_campo(self, rotulo, valor_atual=None):
        if valor_atual is not None:
            prompt = f"{rotulo} [{Fore.GREEN}{valor_atual}{Style.RESET_ALL}]: "
        else:
            prompt = f"{rotulo}: "
        valor = input(prompt)
        if valor == "" and valor_atual is not None:
            return valor_atual
        return valor      
      
    def ler_dados_cliente(self, cliente_existente=None):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE CLIENTE ===")
        nome = self.ler_campo("Nome do cliente", cliente_existente.nome if cliente_existente else None)
        data_nascimento = self.ler_campo("Data de nascimento", Data_Utils.data_para_string(cliente_existente.data_nascimento) if cliente_existente else None)
        limite_credito = float(self.ler_campo("Limite de crédito", str(cliente_existente.limite_credito) if cliente_existente else None))
        return nome, data_nascimento, limite_credito

    def ler_id(self):
        return input("Digite o ID do cliente: ")
    
    def exibir_clientes(self, clientes):
        print(Fore.YELLOW + "\n--- TABELA DE CLIENTES ---")
        if not clientes:
            print("Nenhum cliente cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'DATA DE NASCIMENTO':<20} | { 'IDADE':<10} | {'LIMITE DE CRÉDITO':<10}")
        print("-"*73)
        for c in clientes:
            print(f"{c.id:<4} | {c.nome:<20} | {Data_Utils.data_para_string(c.data_nascimento):<20} | {c.idade:<10} | {c.limite_credito:<10.2f}")
        print("-"*73)
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")


