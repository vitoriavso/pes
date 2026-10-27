'''3 - VagaDeEstacionamento e Carro (0..1 - Associação Simples)
Objetivo: Modelar um relacionamento 0..1 onde a "parte" (Carro) vem de fora
(Agregação/Associação).
Classes: Carro e VagaDeEstacionamento.
Regras:
A classe Carro é simples, tem apenas placa e modelo.
• A classe VagaDeEstacionamento tem um id_vaga (ex: "A-101").
• Uma VagaDeEstacionamento pode estar ocupada por zero ou um Carro (0..1). O
atributo carro_estacionado começa como None.
• Crie um método ocupar_vaga(carro_obj). Este método deve verificar se a vaga já
está None. Se estiver livre, associa o carro_obj (vindo de fora) à vaga e retorna
True. Se já estiver ocupada, não faz nada e retorna False.
• Crie um método liberar_vaga() que simplesmente seta carro_estacionado de volta
para None.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo VagaDeEstacionamento.'''


from minhasclasses7 import VagaDeEstacionamento, Carro


# Programa principal

vagas = []

for i in range(1, 21):
    vaga = VagaDeEstacionamento(f"A-{i:03d}")
    vagas.append(vaga)

print("\n\n=== ESTACIONAMENTO ===")
print("Temos 20 vagas disponíveis!\n")

while True:
    print("\n=== MENU ===")
    print("1 - Estacionar carro")
    print("2 - Consultar vagas")
    print("3 - Liberar vaga")
    print("4 - Sair\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nVagas livres:")

        for vaga in vagas:
            if vaga.carro_estacionado is None:
                print(vaga.id_vaga)

        codigo = input("\nDigite o código da vaga desejada: ")

        vaga_escolhida = None

        for vaga in vagas:
            if vaga.id_vaga == codigo:
                vaga_escolhida = vaga
                break

        if vaga_escolhida is None:
            print("Código de vaga inválido!")

        elif vaga_escolhida.carro_estacionado is not None:
            print("Essa vaga já está ocupada!")

        else:
            placa = input("Digite a placa do carro: ")
            modelo = input("Digite o modelo do carro: ")

            carro = Carro(placa, modelo)

            if vaga_escolhida.ocupar_vaga(carro):
                print("Carro estacionado com sucesso!")
                print("Vaga:", vaga_escolhida.id_vaga)

    elif opcao == "2":
        print("\n=== SITUAÇÃO DAS VAGAS ===")

        livres = 0
        ocupadas = 0

        for vaga in vagas:
            if vaga.carro_estacionado is None:
                print(vaga.id_vaga, "- Livre")
                livres += 1
            else:
                print(vaga.id_vaga, "- Ocupada")
                ocupadas += 1

        print("\nVagas livres:", livres)
        print("Vagas ocupadas:", ocupadas)

    elif opcao == "3":
        codigo = input("Digite o código da vaga a liberar: ")

        vaga_escolhida = None

        for vaga in vagas:
            if vaga.id_vaga == codigo:
                vaga_escolhida = vaga
                break

        if vaga_escolhida is None:
            print("Código de vaga inválido!")

        elif vaga_escolhida.carro_estacionado is None:
            print("Essa vaga já está livre!")

        else:
            vaga_escolhida.liberar_vaga()
            print("Vaga liberada com sucesso!")

    elif opcao == "4":
        print("Encerrando o estacionamento...")
        break

    else:
        print("Opção inválida! Tente novamente.")
