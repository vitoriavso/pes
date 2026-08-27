'''5 – Desenvolva uma calculadora que leia dois números e apresente o seguinte menu:
• 1 – Adição;
• 2 – Subtração;
• 3 – Multiplicação;
• 4 – Divisão;
• 0 – Sair.
Realize a operação escolhida e exiba o resultado. Caso a opção seja inválida, apresente uma
mensagem de erro. O menu deve ser exibido novamente até que o usuário escolha a opção 0.'''

while True:
    print("\n--- MENU ---")
    print("1 – Adição")
    print("2 – Subtração")
    print("3 – Multiplicação")
    print("4 – Divisão")
    print("0 – Sair")

    opcao = (int(input("Escolha uma opção: ")))

    if opcao == 0:
        print("Programa encerrado.")
        break
    elif opcao in [1, 2, 3, 4]:
        num1 = (float(input("Digite o primeiro número: ")))
        num2 = (float(input("Digite o segundo número: ")))

        if opcao == 1:
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif opcao == 2:
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif opcao == 3:
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif opcao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida! Tente novamente.")