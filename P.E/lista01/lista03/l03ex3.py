'''3 – Faça um programa que funcionará como um cadastro de códigos de produtos de uma
loja de roupas. O cadastro deve ser realizado em uma lista com até 10 códigos. Inicialize
os elementos da lista com -1, este valor indicará que o elemento está vago para o
cadastro. Seu programa deve ter um menu com uma opção para cadastrar um novo
código (apenas um por vez) e para listar os todos códigos cadastrados (não devem ser
listados códigos não cadastrados). Deve-se também informar se houve sucesso ou falha
na hora de cadastrar um novo código e também não deve ser possível cadastrar um
produto com o código -1. No momento do cadastro, não deve ser informado o valor do
índice, esse deve ser “calculado” automaticamente. Veja como deve ser criado o menu:
Menu
----
1 – Cadastrar
2 – Listar todos
0 – Sair'''

codigos = [-1] * 10

#posição do indice
posicao = 0



while True:
    print('\nMENU','\n----', '\n1 – Cadastrar', '\n2 – Listar todos', '\n0 – Sair')
    op = int(input('Digite a opção: '))

    if op == 1:
        if posicao < 10:
            codigo = int(input('Digite o codigo do produto: '))
            if codigo != -1:
                codigos[posicao] =  codigo
                posicao = posicao + 1
                print('código cadastrado com sucesso!')
            else:
                print('Código inválido.')
        else:
            print('Não há mais espaço para armazenar códigos.')
    elif op == 2:
        print('\nCódigos cadastrados:')
        for codigo in codigos:
            if codigo != -1:
                print(codigo)

    elif op == 0:
        print('Você saiu do programa.')
        break

    else:
        print('Opção inválida.')
