from colorama import init, Fore, Style
from app.core.data_utils import Data_Utils

init(autoreset=True)


class Usuario_Terminal_View:

    def __init__(self):
        self.titulo_sistema = "=== CRUD DE USUÁRIOS (MVC) ==="

    def renderizar_menu(self):

        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Excluir usuário")
        print("0 - Sair")
        print(Fore.CYAN + "=" * 70)

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

        print(Fore.CYAN + Style.BRIGHT + "=== DADOS DO USUÁRIO ===")

        nome = self.ler_campo(
            "Nome",
            usuario_existente.nome if usuario_existente else None
        )

        email = self.ler_campo(
            "E-mail",
            usuario_existente.email if usuario_existente else None
        )

        data_nascimento = self.ler_campo(
            "Data de nascimento",
            Data_Utils.data_para_string(
                usuario_existente.data_nascimento
            ) if usuario_existente else None
        )

        return nome, email, data_nascimento

    def exibir_cidades(self, cidades):

        print(Fore.YELLOW + "\n--- CIDADES DISPONÍVEIS ---")

        print(
            f"{'ID':<4} | "
            f"{'CIDADE':<30} | "
            f"{'UF':<4}"
        )

        print("-" * 45)

        for cidade in cidades:

            print(
                f"{cidade.id:<4} | "
                f"{cidade.nome:<30} | "
                f"{cidade.estado.sigla:<4}"
            )

        print("-" * 45)

    def ler_cidade(self, cidade_atual=None):

        if cidade_atual is None:
            return input("Informe o ID da cidade: ")

        valor = input(
            f"Cidade [{Fore.GREEN}{cidade_atual}{Style.RESET_ALL}]: "
        )

        if valor == "":
            return cidade_atual

        return valor

    def ler_id(self):

        return input("Digite o ID do usuário: ")

    def exibir_usuarios(self, usuarios):

        print(Fore.YELLOW + "\n--- TABELA DE USUÁRIOS ---")

        if not usuarios:

            print("Nenhum usuário cadastrado.")
            return

        print(
            f"{'ID':<4} | "
            f"{'NOME':<20} | "
            f"{'EMAIL':<35} | "
            f"{'NASCIMENTO':<12} | "
            f"{'IDADE':<5} | "
            f"{'CIDADE':<20} | "
            f"{'UF':<3}"
        )

        print("-" * 125)

        for usuario in usuarios:

            print(
                f"{usuario.id:<4} | "
                f"{usuario.nome:<20} | "
                f"{usuario.email:<35} | "
                f"{Data_Utils.data_para_string(usuario.data_nascimento):<12} | "
                f"{usuario.idade:<5} | "
                f"{usuario.cidade.nome:<20} | "
                f"{usuario.cidade.estado.sigla:<3}"
            )

        print("-" * 125)

    def exibir_mensagem(self, mensagem, sucesso=True):

        cor = Fore.GREEN if sucesso else Fore.RED

        print(cor + f"\n[STATUS] {mensagem}\n")

        self.aguardar_entrada()

    def aguardar_entrada(self):

        input(Fore.WHITE + "Pressione Enter para continuar...")