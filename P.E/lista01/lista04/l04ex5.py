'''5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.
Crie um menu, conforme abaixo, para permitir a interação com o seu programa:
Amigos Próximos
---------------
1 - Cadastrar
2 - Excluir
3 - Listar
0 - Sair'''
print("")
print('--- Atualização do Close Friends ---')
print('Escolha uma opção abaixo:')

cfs = []

indice = 0

while True:
    print('\nMENU','\n----', '\n1 – Cadastrar', '\n2 - Excluir','\n3 - Listar', '\n0 - Sair')
    op = int(input('Digite a opção: '))

    if op == 1:
        nome = input("Digite o nome: ")
        if nome in cfs:
            print('Amigo/a já cadastrado/a.')
        else:
            cfs.append(nome)
            print('Amigo/a cadastrado com sucesso! :)')
            indice = indice + 1
    elif op == 2:
        print('Remova uma amigo/a.')
        exclui =input('Qual amigo/a você removerá? ')

        if exclui in cfs:
            print("Excluindo...")
            cfs.remove(exclui)
        else:
            print('Não foi possível excluir este amigo/a, pois ele/a não existe no nosso sistema!')
    
    elif op == 3:
        quantidade = len(cfs)
        indice = 0
        if quantidade == 0:
            print('A seu Close Friends está vazio :(')
        else:
            while indice < quantidade:
                print("Amigo/a: ", cfs[indice])
                indice = indice + 1
    
    elif op == 0:
        print('Saindo do programa...')
        break
    
    else:
        print("Opção inválida")
        print ('Inicie o programa novamente')