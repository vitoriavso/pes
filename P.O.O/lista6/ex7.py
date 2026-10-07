'''7 – Utilizando como base o exercício anterior, inclua no menu mais duas opções: uma
para excluir uma pessoa baseada no seu nome e outra para atualizar a idade, altura e
peso, baseado, também, no nome informado.'''

from minhas_classes import Pessoa

# uma só
pessoas = []

while True:
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Atualizar Dados")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        pessoa = Pessoa(nome, idade, altura, peso)
        pessoas.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in pessoas:
                print("-------------------")
                print("Nome:", pessoa.nome)
                print("Idade:", pessoa.idade)
                print("Altura:", pessoa.altura)
                print("Peso:", pessoa.peso)

    elif opcao == "3":
        nome = input("Digite o nome da pessoa que deseja excluir: ")

        encontrada = False

        for pessoa in pessoas:
            if pessoa.nome == nome:
                pessoas.remove(pessoa)
                encontrada = True
                print("Pessoa excluída com sucesso!")
                break

        if encontrada == False:
            print("Pessoa não encontrada.")

    elif opcao == "4":
        nome = input("Digite o nome da pessoa que deseja atualizar: ")

        encontrada = False

        for pessoa in pessoas:
            if pessoa.nome == nome:
                pessoa.idade = int(input("Nova idade: "))
                pessoa.altura = float(input("Nova altura: "))
                pessoa.peso = float(input("Novo peso: "))

                encontrada = True
                print("Dados atualizados com sucesso!")
                break

        if encontrada == False:
            print("Pessoa não encontrada.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")