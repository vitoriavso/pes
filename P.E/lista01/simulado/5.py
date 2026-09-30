'''5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
• 1 – Adição;
• 2 – Subtração;
• 3 – Multiplicação;
• 4 – Divisão;
• 0 – Sair.
Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.'''

print ('\n-------- Seja bem-vinda(o), experimente a calculadora Ortiz. --------\n')

while True:
    print('---------Menu--------')
    print('|• 1 - Adição        |')
    print('|• 2 – Subtração     |')
    print('|• 3 – Multiplicação |')
    print('|• 4 – Divisão       |')
    print('|• 0 – Sair.         |')
    print('----------------------')
    operacao = input('Qual operação você deseja fazer? ')
    
    if operacao == '0':
        print ('\n Saindo da calculadora .... \n')
        break
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite um outro número: '))

    if operacao == '1':
        result = n1 + n2
        print('A adição dos dois números é: ', result)
        op = input('Você deseja fazer outra operação(s/n)? ')
        if op == 'n':
            print('\n Saindo da calculadora .... \n')
            break
        else:
            continue

    elif operacao == '2':
        result = n1 - n2
        print('A subtração dos dois números é: ', result)
        op = input('Você deseja fazer outra operação(s/n)? ')
        if op == 'n':
            print('\n Saindo da calculadora .... \n')
            break
        else:
            continue

    elif operacao == '3':
        result = n1 * n2
        print('A multiplicação dos dois números é: ', result)
        op = input('Você deseja fazer outra operação(s/n)? ')
        if op == 'n':
            print('\n Saindo da calculadora .... \n')
            break
        else:
            continue

    elif operacao == '4':
        if n2 == 0:
            print('Não é possível fazer divisão com o número 0.')
            break
        result = n1 / n2
        print('A divisão dos dois números é: ', result)
        op = input('Você deseja fazer outra operação(s/n)? ')
        if op == 'n':
            print('\n Saindo da calculadora .... \n')
            break
        else:
            continue