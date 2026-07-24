import os

from app.models.cliente import Cliente
from app.core.data_utils import Data_Utils


class Cliente_Controller:

    def __init__(self, dao, cidade_dao, view):
        self.dao = dao
        self.cidade_dao = cidade_dao
        self.view = view

    def save(self):

        try:

            cidades = self.cidade_dao.get_all()

            if not cidades:

                self.view.exibir_mensagem(
                    "Cadastre uma cidade antes de cadastrar clientes.",
                    False
                )

                return

            self.view.exibir_cidades(cidades)

            id_cidade = int(self.view.ler_cidade())

            cidade = self.cidade_dao.get_by_id(id_cidade)

            if cidade is None:

                self.view.exibir_mensagem(
                    "Cidade não encontrada.",
                    False
                )

                return

            nome, data_nascimento, limite_credito = \
                self.view.ler_dados_cliente()

            cliente = Cliente(
                None,
                nome,
                Data_Utils.string_para_data(data_nascimento),
                limite_credito,
                cidade
            )

            self.dao.save(cliente)

            self.view.exibir_mensagem(
                "Cliente cadastrado com sucesso!"
            )

        except ValueError:

            self.view.exibir_mensagem(
                "Erro: Entrada inválida. Tente novamente.",
                False
            )

        except KeyboardInterrupt:

            self.view.exibir_mensagem(
                "Operação cancelada pelo usuário.",
                False
            )

    def get_all(self):

        clientes = self.dao.get_all()

        self.view.exibir_clientes(clientes)

        self.view.aguardar_entrada()

    def update(self):

        try:

            clientes = self.dao.get_all()

            self.view.exibir_clientes(clientes)

            id_cliente = int(self.view.ler_id())

            cliente_existente = self.dao.get_by_id(id_cliente)

            if cliente_existente is None:

                self.view.exibir_mensagem(
                    "Cliente não encontrado.",
                    False
                )

                return

            cidades = self.cidade_dao.get_all()

            self.view.exibir_cidades(cidades)

            id_cidade = self.view.ler_cidade(
                cliente_existente.cidade.id
            )

            cidade = self.cidade_dao.get_by_id(
                int(id_cidade)
            )

            if cidade is None:

                self.view.exibir_mensagem(
                    "Cidade não encontrada.",
                    False
                )

                return

            nome, data_nascimento, limite_credito = \
                self.view.ler_dados_cliente(
                    cliente_existente
                )

            cliente_existente.atualizar_dados(
                nome,
                Data_Utils.string_para_data(
                    data_nascimento
                ),
                limite_credito,
                cidade
            )

            self.dao.update(cliente_existente)

            self.view.exibir_mensagem(
                "Cliente atualizado com sucesso!"
            )

        except ValueError as e:

            self.view.exibir_mensagem(
                f"Erro: {str(e)}",
                False
            )

    def delete(self):

        try:

            clientes = self.dao.get_all()

            self.view.exibir_clientes(clientes)

            id_cliente = int(self.view.ler_id())

            sucesso = self.dao.delete(id_cliente)

            if sucesso:

                self.view.exibir_mensagem(
                    "Cliente excluído com sucesso!"
                )

            else:

                self.view.exibir_mensagem(
                    "Cliente não encontrado.",
                    False
                )

        except ValueError:

            self.view.exibir_mensagem(
                "Erro: ID inválido",
                False
            )

    def inicializar_sistema(self):

        while True:

            os.system(
                'cls'
                if os.name == 'nt'
                else 'clear'
            )

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

                self.view.exibir_mensagem(
                    "Opção inválida. Tente novamente.",
                    False
                )