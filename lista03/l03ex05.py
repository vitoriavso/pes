'''5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
ser através de um menu com as seguintes opções:
1 – Cadastrar
2 - Excluir
3 - Alterar
4 - Listar
0 - Sair
A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
das pessoas cadastradas. '''

nomes = [] 
idds = []
alts = []
pesos = []

# posição livre em nome
posicaonome = 0
# posição livre em idade
posicaoidade = 0
# posição livre em altura
posicaoaltura = 0
# posição livre em peso
posicaopeso = 0

inf = input('Qual informação você deseja armazenar?')

while True:

    while inf == nomes:
        print('\nMENU','\n----', '\n1 – Cadastrar', '\n2 - Excluir','\n3 - Alterar', '\n4 - Listar', '\n0 - Sair')
        op = int(input('Digite a opção: '))


        if op == 1:
            if 0 in nomes:  # se tiver espaço livre

                posicaonome = nomes.index(0)

                nome = input('Digite a placa: ')

                if nome != "":

                    if nome in nomes:
                        print('Nome já cadastrado.')

                    else:
                        nomes[posicaonome] = nome
                        print('Nome cadastrado com sucesso!')

                else:
                    print('Nome Inválido.')

            else:
                print('Não há mais espaço para armazenar placas.')

        elif op == 2:
            exclui = input('Qual nome deseja excluir? ')

            if exclui in nomes:
                indice = nomes.index(exclui)
                nomes[indice] = 0
                print('Nome excluído com sucesso!')

            else:
                print('Não foi possível excluir este nome, pois ele não existe no nosso sistema!')

        elif op == 3:
            nomealtrd = input('Qual nome deseja alterar? ')

            if nomealtrd in nomes:
                indice = nomes.index(nomealtrd)
                nomes[indice] = input('Qual será o nome alterado?')
                print('Nome alterado com sucesso!')

        elif op == 4:
            print('\nListando...')
            print('\nNomes Cadastrados:')

            for nome in nomes:
                if nome != 0:
                    print(nome)

        elif op == 0:
            print('Você saiu do programa.')
            break

        else:
            print('Opção inválida.')


    while inf == idds:
        print('\nMENU','\n----', '\n1 – Cadastrar', '\n2 - Excluir','\n3 - Alterar', '\n4 - Listar', '\n0 - Sair')
        op = int(input('Digite a opção: '))


        if op == 1:
            if 0 in idds:  # se tiver espaço livre

                posicaoidade = idds.index(0)

                idd = input('Digite a placa: ')

                if idd != "":

                    if idd in idds: # idd variavel e idds lista
                        print('Idade já cadastrado.')

                    else:
                        idds[posicaoidade] = idd
                        print('Idade cadastrada com sucesso!')

                else:
                    print('Idade inválida.')

            else:
                print('Não há mais espaço para armazenar placas.')

        elif op == 2:
            exclui = input('Qual nome deseja excluir? ')

            if exclui in nomes:
                indice = nomes.index(exclui)
                nomes[indice] = 0
                print('Nome excluído com sucesso!')

            else:
                print('Não foi possível excluir este nome, pois ele não existe no nosso sistema!')

        elif op == 3:
            nomealtrd = input('Qual nome deseja alterar? ')

            if nomealtrd in nomes:
                indice = nomes.index(nomealtrd)
                nomes[indice] = input('Qual será o nome alterado?')
                print('Nome alterado com sucesso!')

        elif op == 4:
            print('\nListando...')
            print('\nPlacas cadastradas:')

            for nome in nomes:
                if nome != 0:
                    print(nome)

        elif op == 0:
            print('Você saiu do programa.')
            break

        else:
            print('Opção inválida.')
