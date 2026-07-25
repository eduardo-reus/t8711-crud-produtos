from app.models.cliente import Cliente
from app.core.data_utils import Data_Utils

class Cliente_Controller:

    def __init__(
        self,
        dao,
        cidade_dao,
        estado_dao,
        view
    ):
        self.dao = dao
        self.cidade_dao = cidade_dao
        self.estado_dao = estado_dao
        self.view = view

    def save(self):

        estados = self.estado_dao.get_all()

        if not estados:

            self.view.exibir_mensagem(
                "Cadastre um estado antes de cadastrar clientes.",
                False
            )

            return

        self.view.exibir_estados(estados)

        id_estado = int(self.view.ler_estado())

        cidades = self.cidade_dao.get_by_estado(id_estado)

        if not cidades:

            self.view.exibir_mensagem(
                "Não existem cidades cadastradas para esse estado.",
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

        nome, data_nascimento, limite_credito = (
            self.view.ler_dados_cliente()
        )

        cliente = Cliente(
            None,
            nome,
            Data_Utils.string_para_data(data_nascimento),
            limite_credito,
            cidade
        )

        self.dao.save(cliente)

        self.view.exibir_mensagem(
            "Cliente cadastrado com sucesso."
        )

    def get_all(self):

        clientes = self.dao.get_all()

        self.view.exibir_clientes(clientes)

        self.view.aguardar_entrada()

    def update(self):

        id_cliente = int(self.view.ler_id())

        cliente_existente = self.dao.get_by_id(id_cliente)

        if cliente_existente is None:

            self.view.exibir_mensagem(
                "Cliente não encontrado.",
                False
            )

            return

        estados = self.estado_dao.get_all()

        self.view.exibir_estados(estados)

        id_estado = self.view.ler_estado(
            cliente_existente.cidade.estado.id
        )

        cidades = self.cidade_dao.get_by_estado(
            int(id_estado)
        )

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

        nome, data_nascimento, limite_credito = (
            self.view.ler_dados_cliente(
                cliente_existente
            )
        )

        cliente_existente.atualizar_dados(
            nome,
            Data_Utils.string_para_data(data_nascimento),
            limite_credito,
            cidade
        )

        self.dao.update(cliente_existente)

        self.view.exibir_mensagem(
            "Cliente atualizado com sucesso."
        )

    def delete(self):

        id_cliente = int(self.view.ler_id())

        if self.dao.delete(id_cliente):

            self.view.exibir_mensagem(
                "Cliente excluído com sucesso."
            )

        else:

            self.view.exibir_mensagem(
                "Cliente não encontrado.",
                False
            )

    def inicializar_sistema(self):

        while True:

            opcao = self.view.renderizar_menu()

            match opcao:

                case 1:
                    self.save()

                case 2:
                    self.get_all()

                case 3:
                    self.update()

                case 4:
                    self.delete()

                case 0:
                    break

                case _:

                    self.view.exibir_mensagem(
                        "Opção inválida.",
                        False
                    )