'''9 – Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
dados do disco, utilizando como base, o exercício 7.'''

import pickle 
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
    print("5 - Salvar Dados")
    print("6 - Carregar Dados")
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

    elif opcao == "5":
        with open("pessoas.pkl", "wb") as f:
            pickle.dump(pessoas, f)
        print("Dados salvos com sucesso!")

    elif opcao == "6":
        try:
            with open("pessoas.pkl", "rb") as f:
                pessoas = pickle.load(f)
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except Exception as e:
            print("Erro ao carregar dados:", e)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")