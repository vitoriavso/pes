from classese2 import RegistroDeAbertura, Anotacao, Chamado

# PROGRAMA PRINCIPAL

print("=== SISTEMA DE CHAMADOS ===")

# Criando chamado
titulo = input("Dê um título para o chamado: ")
data_hora = input("Digite a data e hora de abertura: ")
descricao = input("Digite a descrição do problema: ")

chamado = Chamado(titulo, data_hora, descricao)

# Menu de opções
opcao = ""

while opcao != "4":

    print("\n=== MENU ===")
    print("1 - Adicionar anotação")
    print("2 - Consultar relato")
    print("3 - Consultar chamado")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        texto = input("Digite a anotação: ")
        autor = input("Digite o nome do autor: ")

        chamado.adicionar_anotacao(texto, autor)

        print("Anotação adicionada com sucesso!")

    elif opcao == "2":

        print("\n", chamado.relato())

    elif opcao == "3":

        print("\n", chamado)

    elif opcao == "4":

        print("Encerrando o programa...")

    else:
        print("Opção inválida!")
