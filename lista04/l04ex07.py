'''7 – Utilizando como base o exercício 6, implemente dois novos recursos: um para
informar a maior nota cadastrada e outro para informar a menor nota cadastrada. Caso
não existam notas cadastradas, seu programa deve informar “Erro: não há notas
cadastradas”. Crie um menu, conforme abaixo, para permitir a interação com o seu
programa:
Notas
-----
1 - Cadastrar
2 - Excluir
3 - Listar
4 - Calcular média
5 – Mostrar maior nota
6 – Mostrar menor nota
0 - Sair
Opção:
'''

print('\n','----- Cadastro de Notas -----', '\n')
print('Escolha uma das opções abaixo:')

notas = []

indice = 0

while True:
    print('\nMENU','\n----', '\n1 – Cadastrar', '\n2 - Excluir','\n3 - Listar', '\n4 - Calcular média', '\n5 - Informar a maior nota cadastrada', '\n6 - Informar a menor nota cadastrada', '\n0 - Sair')
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
            print('\n', 'Listando notas...', '\n')
            print('Lista de notas', '\n')
            print('----------')
            while indice < quantidade:
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

    elif op == 5:
        if len(notas) == 0:
            print('\n', "Erro: não há notas cadastradas.")
        else:
            notas_ordenadas = sorted(notas)
            print('\n', "Maior nota:", notas_ordenadas[len(notas_ordenadas)-1])
    
    elif op == 6:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas.")
        else:
            notas_ordenadas = sorted(notas)
            print('\n', "Menor nota:", notas_ordenadas[0])
    
    elif op == 0:
        print('\n', '\n', '\n', 'Saindo do programa...')
        break
    
    else:
        print('\n', "Opção inválida")
        print ('\n', 'Inicie o programa novamente')