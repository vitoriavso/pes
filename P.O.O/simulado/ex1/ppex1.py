from classesex1 import Notebook, Bancada
# PROGRAMA PRINCIPAL

print("=== SISTEMA DE BANCADAS ===")

# Criando a bancada
numero = input("Digite o número da bancada: ")
bancada = Bancada(numero)

# Criando notebooks
patrimonio = input("\nDigite o patrimônio do primeiro notebook: ")
marca = input("Digite a marca do primeiro notebook: ")
notebook1 = Notebook(patrimonio, marca)

patrimonio = input("\nDigite o patrimônio do segundo notebook: ")
marca = input("Digite a marca do segundo notebook: ")
notebook2 = Notebook(patrimonio, marca)

# Menu de operações
opcao = ""

while opcao != "4":

    print("\n=== MENU ===")
    print("1 - Colocar notebook")
    print("2 - Retirar notebook")
    print("3 - Consultar bancada")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        patrimonio = input("Digite o patrimônio do notebook: ")

        if patrimonio == notebook1.patrimonio:
            notebook = notebook1
        elif patrimonio == notebook2.patrimonio:
            notebook = notebook2
        else:
            notebook = None

        if notebook is None:
            print("Notebook não encontrado!")
        elif bancada.colocar(notebook):
            print("Notebook colocado com sucesso!")
        else:
            print("A bancada já está ocupada!")

    elif opcao == "2":

        if bancada.notebook_atual is None:
            print("A bancada já está vazia!")
        else:
            bancada.retirar()
            print("Notebook retirado com sucesso!")

    elif opcao == "3":

        print(bancada)

    elif opcao == "4":

        print("Encerrando o programa...")

    else:
        print("Opção inválida!")


