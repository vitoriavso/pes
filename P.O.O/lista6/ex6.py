'''6 – Utilizando como base a classe Pessoa do exercício anterior, crie um algoritmo que
funcionará como um cadastro de pessoas em uma lista. Seu algoritmo deve ter um menu
conforme abaixo:
Cadastro de Pessoas
-------------------
1 – Cadastrar
2 – Listar
0 – Sair
Opção: '''

from minhas_classes import Pessoa

# uma só
pessoas = []

while True:
    print('\nCadastro de Pessoas')
    print('-------------------')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('0 - Sair')

    opcao = input('Opção: ')

    if opcao == '1':
        print('Cadastrando pessoa: ')
        n = input('Nome: ')
        i = int(input('Idade: '))
        a = float(input('Altura: '))
        p = float(input('Peso: '))

        pessoa = Pessoa(n, i, a, p)
        pessoas.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            print("\nPessoas cadastradas:")
            print("-------------------")
            for pessoa in pessoas:
                print("Nome:", pessoa.nome)
                print("Idade:", pessoa.idade)
                print("Altura:", pessoa.altura)
                print("Peso:", pessoa.peso)
                print("-------------------")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")