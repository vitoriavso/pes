'''2 - A situação de logística da Empresa Alpha Entregas está necessitando de melhorias no
controle das saídas e retornos dos caminhões:
a) Considere que a empresa possui 8 caminhões numerados de 001 a 008;
b) Cada caminhão tem seu respectivo condutor, a relação dos condutores e seus
códigos está abaixo;
c) As entregas são monitoradas através do controle no retorno de cada caminhão;
d) Precisamos receber os dados do código do caminhão e do código do condutor,
somente assim consideraremos que a mercadoria daquela rota foi entregue;
e) O algoritmo deve prever o cadastro dos caminhões e dos condutores;
f) O algoritmo deve prever um cadastro com uma lista de todos os caminhões que
saem diariamente;
g) A cada saída diária dos caminhões, deve-se registrar a data e hora de saída de
cada veículo, bem como o condutor responsável;
h) Quando do retorno de cada caminhão, deve-se registrar a data e hora de
chegada;
i) O sistema deve ter opções para verificar se um determinado caminhão retornou da
rota ou não, mostrando a data, hora e nome do condutor, consultando por código do
veículo;
j) O sistema deve ter opções para listar o cadastro de caminhões;
k) O sistema deve ter opções para listar os condutores;
l) O sistema deve ter opções para listar, por data, a lista dos veículos que
retornaram;
m) Precisamos saber, em determinado momento, se todas as entregas do dia foram
realizadas.

Relação de Condutores:
001 – Roberto Souza
002 – João Graciano
003 – Karine Silva
004 – Pedro Luiz
005 – Maria Catarina
006 – Júlio Cardoso
007 – Altivo Antônio
008 – Jorge Gonçalves
009 – Marcos Vinícius
010 – Heleno Nunes
011 – Mara Cristina
012 – Otávio Rocha

Relação dos Veículos
001 – Monobloco
002 – Scania 112 HW
003 – Volkswagen Express 4150
004 – Volkswagen Express 6160
005 – Volkswagen VW 17230 Worker
006 – Volkswagen Express 9170
007 – Iveco Daily 40s14
008 – Iveco Tectro 310E28'''

# inicio

caminhoes = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 6160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40S14",
    "008": "Iveco Tector 310E28"
}

# Cadastro dos condutores
condutores = {
    "001": "Roberto Souza",
    "002": "João Graciano",
    "003": "Karine Silva",
    "004": "Pedro Luiz",
    "005": "Maria Catarina",
    "006": "Júlio Cardoso",
    "007": "Altivo Antônio",
    "008": "Jorge Gonçalves",
    "009": "Marcos Vinícius",
    "010": "Heleno Nunes",
    "011": "Mara Cristina",
    "012": "Otávio Rocha"
}

# Lista das viagens
viagens = []

opcao = -1

while opcao != 0:

    print("\n====== EMPRESA ALPHA ENTREGAS ======\n\n\n")
    print("1 - Registrar saída\n")
    print("2 - Registrar retorno\n")
    print("3 - Consultar caminhão\n")
    print("4 - Listar caminhões\n")
    print("5 - Listar condutores\n")
    print("6 - Listar retornos por data\n")
    print("7 - Verificar entregas do dia\n")
    print("0 - Sair\n\n")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':

        cod_cam = input("Código do caminhão: ")
        cod_cond = input("Código do condutor: ")

        if cod_cam not in caminhoes:
            print("Caminhão inexistente.")
            continue

        if cod_cond not in condutores:
            print("Condutor inexistente.")
            continue

        data = input("Data da saída: ")
        hora = input("Hora da saída: ")

        viagem = {
            "caminhao": cod_cam,
            "condutor": cod_cond,
            "data_saida": data,
            "hora_saida": hora,
            "data_chegada": "",
            "hora_chegada": ""
        }

        viagens.append(viagem)

        print("Saída registrada com sucesso!")


    elif opcao == '2':

        cod = input("Código do caminhão: ")

        encontrado = False

        for viagem in viagens:

            if viagem["caminhao"] == cod:

                viagem["data_chegada"] = input("Data da chegada: ")
                viagem["hora_chegada"] = input("Hora da chegada: ")

                print("Retorno registrado!")

                encontrado = True

        if not encontrado:
            print("Caminhão não encontrado.")


    elif opcao == '3':

        cod = input("Código do caminhão: ")

        encontrado = False

        for viagem in viagens:

            if viagem["caminhao"] == cod:

                print("\nCaminhão:", caminhoes[viagem["caminhao"]])
                print("Condutor:", condutores[viagem["condutor"]])
                print("Saída:", viagem["data_saida"], viagem["hora_saida"])

                if viagem["data_chegada"] == "":
                    print("Situação: Em rota")

                else:
                    print("Chegada:", viagem["data_chegada"], viagem["hora_chegada"])
                    print("Situação: Retornou")

                encontrado = True

        if not encontrado:
            print("Caminhão não encontrado.")


    elif opcao == '4':

        print("\n===== CAMINHÕES =====")

        for codigo in caminhoes:
            print(codigo, "-", caminhoes[codigo])


    elif opcao == '5':

        print("\n===== CONDUTORES =====")

        for codigo in condutores:
            print(codigo, "-", condutores[codigo])


    elif opcao == '6':

        data = input("Digite a data: ")

        encontrou = False

        for viagem in viagens:

            if viagem["data_chegada"] == data:

                print("\nCaminhão:", caminhoes[viagem["caminhao"]])
                print("Condutor:", condutores[viagem["condutor"]])
                print("Hora da chegada:", viagem["hora_chegada"])

                encontrou = True

        if not encontrou:
            print("Nenhum retorno encontrado nessa data.")


    elif opcao == '7':

        if len(viagens) == 0:

            print("Nenhum caminhão saiu hoje.")

        else:

            todas = True

            for viagem in viagens:

                if viagem["data_chegada"] == "":
                    todas = False

            if todas:
                print("Todas as entregas do dia foram realizadas.")

            else:
                print("Ainda existem caminhões em rota.")


    elif opcao == '0':

        print("\nSistema encerrado.\n\n\n")
        break

    else:

        print("Opção inválida!")