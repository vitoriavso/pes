'''6 – Elabore um programa que funcionará como um cadastro notas de um estudante. Seu
programa deve permitir que notas sejam cadastradas ou removidas (através do seu
índice, pois podem haver notas repetidas), conforme a solicitação do usuário. Também
deve ser possível exibir a lista com todas as notas cadastradas, porém, o programa deve
avisar o usuário caso a lista esteja vazia. O programa também deve ter uma opção para
calcular a média do aluno e exibir sua situação (aprovado se média for maior ou igual a 6
e reprovado, caso contrário). Crie um menu, conforme abaixo, para permitir a interação
com o seu programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
0 - Sair
Opção:
'''
print('\n','----- Cadastro de Notas -----', '\n')
print('Escolha uma das opções abaixo:')

notas = []

indice = 0

while True:
    print('\nMENU','\n----', '\n1 – Cadastrar', '\n2 - Excluir','\n3 - Listar', '\n4 - Calcular média', '\n0 - Sair')
    op = int(input('Digite a opção: '))

    if op == 1:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        print('Nota cadastrada com sucesso! :)')
        indice = indice + 1
    elif op == 2:
        if len(notas) == 0:
            print("Não há notas cadastradas.")

        else:
            print('\n')
            print('--------------')
            print("Índice - Nota")
            print('______________')
            indice = 0

            while indice < len(notas):
                print('|',indice, "-", notas[indice], ' ', ' ', ' ', '|')
                indice = indice + 1
            print('--------------', '\n')
            indice = int(input("Digite o índice da nota que deseja excluir: "))

            if indice >= 0 and indice < len(notas):
                notas.pop(indice)
                print("Nota excluída com sucesso!")
            else:
                print("Índice inválido!")
    
    elif op == 3:
        print('\n')
        quantidade = len(notas)
        indice = 0
        if quantidade == 0:
            print('Lista de notas vazia!')
        else:
            while indice < quantidade:
                print('\n', 'Listando notas...', '\n')
                print('Lista de notas', '\n')
                print('----------')
                print('|', "Nota: ", notas[indice], '|')
                indice = indice + 1
    
    elif op == 4:
        print('\n')
        if len(notas) == 0:
            print("Nenhuma nota cadastrada.")

        else:
            soma = 0
            indice = 0

            while indice < len(notas):
                soma = soma + notas[indice]
                indice = indice + 1

            media = soma / len(notas)

            print("Média:", media)

            if media >= 6:
                print('\n', "Situação: Aprovado")
            else:
                print('\n', "Situação: Reprovado")

    elif op == 0:
        print('Saindo do programa...')
        break
    
    else:
        print("Opção inválida")
        print ('Inicie o programa novamente')