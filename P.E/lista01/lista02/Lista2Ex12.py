'''12 – Implemente um programa que funcione como uma calculadora entre dois números
informados. Seu programa deve exibir um menu que solicite a operação a ser realizada
entre dois números (adição, subtração, divisão e multiplicação) e os dois números a
serem utilizados no cálculo. Se o usuário digitar uma opção inválida, deve alertar o
usuário e exibir o menu novamente. Utilize um menu, como o abaixo, no seu programa:
Menu
-------
1 – Adição
2 – Subtração
3 – Divisão
4 – Multiplicação
0 - Sair
Digite a opção:'''

while True:
    print("\nMenu")
    print("-------")
    print("1 – Adição")
    print("2 – Subtração")
    print("3 – Divisão")
    print("4 – Multiplicação")
    print("0 - Sair")

    opcao = input("Digite a opção: ")

    if opcao == "0":
        print("Encerrando o programa...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Tente novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == "1":
        print("Resultado:", num1 + num2)
    elif opcao == "2":
        print("Resultado:", num1 - num2)
    elif opcao == "3":
        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print("Resultado:", num1 / num2)
    elif opcao == "4":
        print("Resultado:", num1 * num2)