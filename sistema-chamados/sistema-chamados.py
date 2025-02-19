"""
Esse programa é um sistema de chamados.

[x] Cadastrar novos chamados
[] Buscar chamados por ID ou descrição
[x] Remover chamados finalizados
[x] Listar chamados em ordem de prioridade
[] Exibir estatísticas sobre os chamados 
"""

from prettytable import PrettyTable

class SistemaChamados(PrettyTable): 
    """
    Essa class faz sistemas de chamados
    """

    def __init__(self, field_names = None, **kwargs):
        super().__init__(field_names, **kwargs)

        self.tabela = PrettyTable()
        self.tabela.field_names = ['ID', 'Prioridade', 'Descrição']


    def cadastrar(self, ID, prioridade, descricao):
        """Essa função cadastra chamados"""
        self.tabela.add_row([ID, prioridade, descricao])

    def buscar(self, metodo: str):
        """Essa função busca chamados baseada em 
        dois métodos: ID e descrição"""
        pass

    def remover(self, index):
        """Essa função remove chamados finalizados"""
        self.tabela.del_row(index)

    def listagem(self):
        """Essa função lista os chamados em ordem de prioridade"""
        print(self.tabela)

    def listagem_prioridade(self):
        """Essa função lista os chamados por ordem de prioridade"""
        print(self.tabela.get_string(sortby="Prioridade"))

    def estatisticas(self):
        """Essa função exibi estatísticas sobre os chamados"""


instancia = SistemaChamados()
instancia.cadastrar('1234', 1, "Meu computador está com problema")
instancia.cadastrar('5587', 3, "alguma coisa")
instancia.cadastrar('2933', 2, "outra coisa")
instancia.cadastrar('0001', 2, "mais uma coisa")

# instancia.remover(2)
instancia.listagem()
print("\nTabela listada por ordem de prioridade")
instancia.listagem_prioridade()



