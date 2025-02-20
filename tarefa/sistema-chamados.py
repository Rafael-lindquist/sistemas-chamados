import json
from prettytable import PrettyTable

with open('bancodedados.json', 'r') as f:
    dados = json.load(f)

class SistemaChamados(PrettyTable): 
    """
    Essa class faz sistemas de chamados
    """

    def __init__(self,):
        super().__init__()
        pass

    def menu(self):
        print("---------------------------")
        print("|   Menu                  |")
        print('---------------------------')
        print("| 1) cadastrar            |")
        print("| 2) remover              |")
        print("| 3) buscar por id        |")
        print("| 4) buscar por descricao |")
        print("| 5) listagem             |")
        print("| 6) listagem prioridade  |")
        print("| 7) listagem invertida   |")
        print("| 8) estatísticas         |")
        print("| digite 'q' para sair    |")
        print('---------------------------')

    def cadastrar(self, prioridade, descricao):
        """Essa função cadastra chamados"""
        id = 0
        for i in dados:
            if i[0] == id:
                id+=1
        chamado = [id, prioridade, descricao]
        dados.append(chamado)
        print(f"Seu chamado foi realizado com sucesso.")

    def buscar_id(self, id):
        """Essa função busca chamados baseada em 
        dois métodos: ID e descrição"""
        if id in [d[0] for d in dados]:
            chamado = [x for x in dados if x[0] == id][0]
            self.tabela = PrettyTable()
            self.tabela.field_names = ['ID', 'Prioridade', 'Descrição']
            self.tabela.add_row(chamado)
            print(self.tabela)
        else:
            print("Esse id não corresponde a nenhum chamado")

    def buscar_descricao(self, descricao):
        """Essa função busca chamados baseada em 
        dois métodos: ID e descrição"""
        if descricao in [d[2] for d in dados]:
            chamado = [x for x in dados if x[2] == descricao][0]
            self.tabela = PrettyTable()
            self.tabela.field_names = ['ID', 'Prioridade', 'Descrição']
            self.tabela.add_row(chamado)
            print(self.tabela)
        else:
            print("Essa descricao não corresponde a nenhum chamado")

    def remover(self, index):
        """Essa função remove chamados finalizados"""
        if index in [d[0] for d in dados]:
            for x in dados:
                if x[0] == index:
                    dados.remove(x)
        else:
            print("Esse id não corresponde a nenhum chamado") 

    def listagem(self):
        """Essa função lista os chamados em ordem de prioridade"""
        self.tabela = PrettyTable()
        self.tabela.field_names = ['ID', 'Prioridade', 'Descrição']
        for i in dados:
            self.tabela.add_row(i)
        print(self.tabela)


    def listagem_prioridade(self):
        """Essa função lista os chamados por ordem de prioridade"""
        self.tabela = PrettyTable()
        self.tabela.field_names = ['ID', 'Prioridade', 'Descrição']
        for i in sorted(dados, key= lambda x: x[1]):
            self.tabela.add_row(i)
        print(self.tabela)

    def estatisticas(self):
        """Essa função exibi estatísticas sobre os chamados"""
        print(f'chamados prioridade 1: {len([x for x in dados if x[1] == '1'])}')
        print(f'chamados prioridade 2: {len([x for x in dados if x[1] == '2'])}')
        print(f'chamados prioridade 3: {len([x for x in dados if x[1] == '3'])}')
        prioridades = [int(x[1]) for x in dados]
        media = sum(prioridades)/len(prioridades)
        variancia = sum([(x - media)**2 for x in prioridades]) / (media - 1)
        print(f'desvio padrão das prioridades: {variancia**(1/2)}')
        print(f'numero total de chamados: {len(dados)}')

    def inverter_dados(self):
        """Essa função inverte os dados"""
        self.tabela = PrettyTable()
        self.tabela.field_names = ['ID', 'Prioridade', 'Descrição']
        for i in sorted(dados, reverse=True):
            self.tabela.add_row(i)
        print(self.tabela)

instancia = SistemaChamados()

while True:
    instancia.menu()
    while True:
        num = input("Digite um número do menu: ")
        if num in ['1','2','3','4','5','6','7','8','q']:
            break
        else:
            print("Insira um número de 1-8 ou 'q'")

    if num == 'q':
        break

    elif num == '1':
        while True:
            prioridade = input('Prioridades:\n1 - muito importante\n2 - importante' \
                                    '\n3 - menos importante\nInsira a sua prioridade: ')
            if prioridade in ['1', '2', '3']:
                break
            else:
                print("A prioridade deve ser um número entre 1, 2 ou 3")
        descricao = input("Insira a descrição: ")
        instancia.cadastrar(prioridade, descricao.lower())

    elif num == '2':
        while True:
            try:
                remover = int(input("Insira o id do chamado para remover: "))
                if remover in [x[0] for x in dados]:
                    break
                else:
                    print('insira um id válido')
            except Exception as e:
                    print("Insira um id válido")
        instancia.remover(remover)

    elif num == '3':
        while True:
            try:
                buscar_id = int(input("Insira o id do chamado para buscar: "))
                if buscar_id in [x[0] for x in dados]:
                    break
                else:
                    print('insira um id válido')
            except Exception as e:
                    print("Insira um id válido")
        instancia.buscar_id(buscar_id)

    elif num == '4':
        buscar_desc = input("Insira a descrição do chamado para buscar: ")
        instancia.buscar_descricao(buscar_desc.lower())

    elif num == '5':
        instancia.listagem()

    elif num == '6':
        instancia.listagem_prioridade()
    
    elif num == '7':
        instancia.inverter_dados()
    elif num == '8':
        instancia.estatisticas()

with open('bancodedados.json', 'w') as f:
    f.write(json.dumps(dados))

"""
Coisas que faltam fazer

- colocar os try except (2, 3, 4)
"""