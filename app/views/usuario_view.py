from colorama import init, Fore, Style
from app.core.data_utils import Data_Utils

init(autoreset=True)

class Usuario_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE USUÁRIOS (MVC) ==="
    
    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar usuário")
        print(f"2 - Listar usuários")
        print(f"3 - Atualizar usuário")
        print(f"4 - Excluir usuário")
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
            
    def ler_dados_usuario(self, usuario_existente=None):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE USUÁRIO ===")
        nome = self.ler_campo("Nome", usuario_existente.nome if usuario_existente else None)
        email = self.ler_campo("E-mail", usuario_existente.email if usuario_existente else None)
        data_nascimento = self.ler_campo("Data de nascimento", Data_Utils.data_para_string(usuario_existente.data_nascimento) if usuario_existente else None)
        return nome, email, data_nascimento

    def ler_id(self):
        return input("Digite o ID do usuário: ")
    
    def exibir_usuarios(self, usuarios):
        print(Fore.YELLOW + "\n--- TABELA DE USUÁRIOS ---")
        if not usuarios:
            print("Nenhum usuário cadastrado")
            return
        print(f"{'ID':<4} | {'NOME':<20} | {'EMAIL':<40} | {'DATA NASCIMENTO':<12}")
        print("-"*75)
        for u in usuarios:
            print(f"{u.id:<4} | {u.nome:<20} | {u.email:<40} | {Data_Utils.data_para_string(u.data_nascimento):<12}")
        print("-"*75)
    
    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")


