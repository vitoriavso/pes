'''10 – Utilizando a biblioteca pickle, implemente duas novas opções para salvar e carregar
dados do disco, utilizando como base, o exercício 8.'''

import pickle
from minhas_classes import Estudante2, Professor2

estudantes = []
professores = []

while True:
    print("\nSistema de Cadastro")
    print("-------------------")
    print("1 - Cadastrar estudante")
    print("2 - Cadastrar professor")
    print("3 - Listar estudantes")
    print("4 - Listar professores")
    print("5 - Alterar estudante pela matrícula")
    print("6 - Alterar estudante pelo nome")
    print("7 - Alterar professor pela matrícula")
    print("8 - Alterar professor pelo nome")
    print("9 - Excluir estudante pela matrícula")
    print("10 - Excluir professor pela matrícula")
    print("11 - Salvar dados no disco")
    print("12 - Carregar dados do disco")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        estudante = Estudante2()
        estudante.nome = input("Nome: ")
        estudante.sobrenome = input("Sobrenome: ")
        estudante.idade = int(input("Idade: "))
        estudante.matricula = input("Matrícula: ")
        estudantes.append(estudante)
        print("Estudante cadastrado com sucesso!")

    elif opcao == "2":
        professor = Professor2()
        professor.nome = input("Nome: ")
        professor.sobrenome = input("Sobrenome: ")
        professor.especializacao = input("Especialização: ")
        professor.matricula = input("Matrícula: ")
        professores.append(professor)
        print("Professor cadastrado com sucesso!")

    elif opcao == "3":
        if not estudantes:
            print("Nenhum estudante cadastrado.")
        else:
            print("Estudantes cadastrados:")
            for est in estudantes:
                print(est.apresentar())

    elif opcao == "4":
        if not professores:
            print("Nenhum professor cadastrado.")
        else:
            print("Professores cadastrados:")
            for prof in professores:
                print(prof.apresentar())

    elif opcao == "5":
        matricula = input("Digite a matrícula do estudante que deseja alterar: ")
        encontrado = False
        for est in estudantes:
            if est.matricula == matricula:
                est.nome = input("Novo nome: ")
                est.sobrenome = input("Novo sobrenome: ")
                est.idade = int(input("Nova idade: "))
                encontrado = True
                print("Estudante alterado com sucesso!")
                break
        if not encontrado:
            print("Estudante não encontrado.")

    elif opcao == "6":
        nome = input("Digite o nome do estudante que deseja alterar: ")
        encontrado = False
        for est in estudantes:
            if est.nome == nome:
                est.sobrenome = input("Novo sobrenome: ")
                est.idade = int(input("Nova idade: "))
                encontrado = True
                print("Estudante alterado com sucesso!")
                break
        if not encontrado:
            print("Estudante não encontrado.")

    elif opcao == "7":
        matricula = input("Digite a matrícula do professor que deseja alterar: ")
        encontrado = False
        for prof in professores:
            if prof.matricula == matricula:
                prof.nome = input("Novo nome: ")
                prof.sobrenome = input("Novo sobrenome: ")
                prof.especializacao = input("Nova especialização: ")
                encontrado = True
                print("Professor alterado com sucesso!")
                break
        if not encontrado:
            print("Professor não encontrado.")

    elif opcao == "8":
        nome = input("Digite o nome do professor que deseja alterar: ")
        encontrado = False
        for prof in professores:
            if prof.nome == nome:
                prof.sobrenome = input("Novo sobrenome: ")
                prof.especializacao = input("Nova especialização: ")
                encontrado = True
                print("Professor alterado com sucesso!")
                break
        if not encontrado:
            print("Professor não encontrado.")

    elif opcao == "9":
        matricula = input("Digite a matrícula do estudante que deseja excluir: ")
        encontrado = False
        for est in estudantes:
            if est.matricula == matricula:
                estudantes.remove(est)
                encontrado = True
                print("Estudante excluído com sucesso!")
                break
        if not encontrado:
            print("Estudante não encontrado.")

    elif opcao == "10":
        matricula = input("Digite a matrícula do professor que deseja excluir: ")
        encontrado = False
        for prof in professores:
            if prof.matricula == matricula:
                professores.remove(prof)
                encontrado = True
                print("Professor excluído com sucesso!")
                break
        if not encontrado:
            print("Professor não encontrado.")

    elif opcao == "11":
        with open("dados.pkl", "wb") as f:
            pickle.dump((estudantes, professores), f)
        print("Dados salvos com sucesso!")

    elif opcao == "12":
        try:
            with open("dados.pkl", "rb") as f:
                estudantes, professores = pickle.load(f)
            print("Dados carregados com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except Exception as e:
            print("Erro ao carregar dados:", e)

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida!")