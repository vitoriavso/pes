'''4 - Codifique um programa que funcionará como um cadastro de placas de automóveis de
um estacionamento (para até 15 automóveis). O cadastro deve ser realizado em uma
lista. Seu programa deve ter um menu com a seguinte estrutura:
1 – Cadastrar
2 - Excluir
3 - Listar
0 - Sair
A opção Cadastrar deve verificar se há espaço disponível na lista para o cadastro. Se
houver, deve proceder o cadastro. Se não, deve informar o usuário que não há espaço
disponível. A opção Excluir deve perguntar ao usuário qual placa deve ser excluída (pelo
nome da placa) e informar se houve sucesso ou falha. Já a opção listar deve
Instituto Federal de Santa Catarina – Reitoria
Rua: 14 de julho, 150 | Coqueiros | Florianópolis /SC | CEP: 88.075-010
Fone: (48) 3877-9000 | www.ifsc.edu.br | CNPJ 11.402.887/0001-60
simplesmente listar todas as placas cadastradas. Dica: utilize um valor padrão para definir
um espaço vago na lista.'''

placas = [0] * 15

#posição do indice
posicao = 0



while True:
    print('\nMENU','\n----', '\n1 – Cadastrar', '\n2 - Excluir','\n3 - Listar', '\n0 - Sair')
    op = int(input('Digite a opção: '))

    if op == 1:
        if posicao < 15:
            placa = input('Digite a placa: ')
            if placa != 0:
                placas[posicao] =  placa
                posicao = posicao + 1
                print('Placa cadastrada com sucesso!')
            else:
                print('Placa inválida.')
        else:
            print('Não há mais espaço para armazenar placas.')
    elif op == 3:
        print('\nListando...')
        print('\nPlacas cadastradas:')
        for placa in placas:
            if placa != 0:
                print(placa)

    elif op == 2:
        exclui = input('Qual palca você deseja excluir?')
        for placa in placas:
            if placa == exclui:
                #placas[placa] = 0
                

    elif op == 0:
        print('Você saiu do programa.')
        break

    else:
        print('Opção inválida.')
