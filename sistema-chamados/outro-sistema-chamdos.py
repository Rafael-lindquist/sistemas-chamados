dados = []

class SistemaChamados(): 
    """
    Essa class faz sistemas de chamados
    """

    def __init__(self,):
        pass 

    def menu(self):
        print("---------------------")
        print("|       Menu         |")
        print('--------------------')
        print("|  1) cadastrar      |")
        print("|  2) remover        |")
        print("|  3) buscar         |")
        print("|  4) listagem       |")
        print("| digite q para sair |")
        print('---------------------')



    def cadastrar(self, ID, prioridade, descricao):
        """Essa função cadastra chamados"""
        dados.append([ID, prioridade, descricao])

    def buscar(self, metodo: str):
        """Essa função busca chamados baseada em 
        dois métodos: ID e descrição"""
        pass

    def remover(self, index):
        """Essa função remove chamados finalizados"""
        pass

    def listagem(self):
        """Essa função lista os chamados em ordem de prioridade"""
        for i in dados:
            print(i)

    def listagem_prioridade(self):
        """Essa função lista os chamados por ordem de prioridade"""
        _dados = sorted(dados, key= lambda x: x[0])
        for i in _dados:
            print(i)

    def estatisticas(self):
        """Essa função exibi estatísticas sobre os chamados"""
        pass

instancia = SistemaChamados()

while True:
    instancia.menu()
    num = input("Digite um número do menu: ")

    if num == 'q':
        break

    elif num == '1':
        id = f"{len(dados) + 1}"
        prioridade = input('Insira a sua prioridade: ')
        descricao = input("Insira a descrição")
        instancia.cadastrar(id, prioridade, descricao)

    elif num == '2':
        remover = input("Insira o id do chamdo para remover: ")
        instancia.remover(remover)

    elif num == '3':
        buscar = input("Insira o id do chamdo para buscar: ")
        instancia.buscar(buscar)

    elif num == '4':
        instancia.listagem()