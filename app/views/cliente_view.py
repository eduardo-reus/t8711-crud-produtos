from colorama import init, Fore, Style

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
        
    def ler_dados_cliente(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE CLIENTE ===")
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento: ")
        limite_credito = float(input("Digite o limite de crédito: "))
        return nome, data_nascimento, limite_credito

    def ler_id(self):
        return input("Digite o ID do cliente: ")
    
    def exibir_clientes(self, clientes):
        print(Fore.YELLOW + "\n--- TABELA DE CLIENTES ---")
        if not clientes:
            print("Nenhum cliente cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'DATA DE NASCIMENTO':<20} | {'LIMITE DE CRÉDITO':<10}")
        print("-"*60)
        for c in clientes:
            print(f"{c.id:<4} | {c.nome:<20} | {c.data_nascimento:<20} | {c.limite_credito:<10.2f}")
        print("-"*60)
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")


