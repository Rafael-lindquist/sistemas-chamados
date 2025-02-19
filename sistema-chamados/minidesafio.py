clientes = {}

def cadastrar(nome: str, idade: int) -> None:
    """Essa função cadastra um cliente"""
    clientes[nome] = idade

def buscar(nome: str) -> None:
    """Essa função busca por um nome"""
    if nome in clientes:
        print("Esse cliente está cadastrado")
        print(f"{nome}: {clientes[nome]} anos")

    else:
        print("Esse cliente não está cadastrado")

def menu():
    """Essa função exibe um menu"""

    print("-------------------------------")
    print("| Digite [1] para Cadastrar   |")
    print("| Digite [2] para Buscar      |")
    print("| Digite [3] para Exibir      |")
    print("| Digite [4] para Sair        |")
    print("-------------------------------")

while True:
    menu()
    numero = input("Digite uma opção: ")
    if numero == '1':
        nome = input("Digite o nome do cliente:")
        try:
            idade = int(input("Digite a idade do cliente: "))
            cadastrar(nome, idade)

        except Exception as e:
            print("Erro: A idade deve ser um número. Tente novamente.\n")

    elif numero == '2':
        nome = input("Qual cliente deseja bucar: ")
        buscar(nome)

    elif numero == '3':
        print("* CLIENTES *")
        print('-----------------------')
        for i in clientes:
            print(f"{i} {clientes[i]}")
        print('-----------------------')
    
    elif numero == '4':
        break

    else:
        print("Não tem essa opção")
