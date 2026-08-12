# Cadastro dos caminhões
cam = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 6160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40s14",
    "008": "Iveco Tectro 310E28"
}

# Cadastro dos condutores
cond = {
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

viagens = []
opcao = "-1"

while opcao != "0": # Corrigido para string "0"

    print("\n====== EMPRESA ALPHA ENTREGAS ======\n")
    print("1 - Registrar saída")
    print("2 - Registrar retorno")
    print("3 - Consultar caminhão")
    print("4 - Listar caminhões")
    print("5 - Listar condutores")
    print("6 - Listar retornos por data")
    print("7 - Verificar entregas do dia")
    print("0 - Sair\n")

    opcao = input("Escolha uma opção: ")

    # Registrar saída
    if opcao == '1':
        cod_cam = input("Código do caminhão: ")
        cod_cond = input("Código do condutor: ")

        if cod_cam not in cam:
            print("Caminhão inexistente.")
            continue

        if cod_cond not in cond:
            print("Condutor inexistente.")
            continue

        # Validação: Impedir saída de caminhão/condutor que já está em rota
        em_rota = False
        for v in viagens:
            if v["data_chegada"] == "":
                if v["caminhao"] == cod_cam:
                    print("Erro: Este caminhão já está em rota!")
                    em_rota = True
                    break
                if v["condutor"] == cod_cond:
                    print("Erro: Este condutor já está em rota!")
                    em_rota = True
                    break

        if em_rota:
            continue

        data = input("Data da saída (DD/MM/AAAA): ")
        hora = input("Hora da saída (HH:MM): ")

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

    # Registrar retorno
    elif opcao == '2':
        cod_cam = input("Código do caminhão: ")
        cod_cond = input("Código do condutor: ")

        if cod_cam not in cam:
            print("Caminhão inexistente.")
            continue

        if cod_cond not in cond:
            print("Condutor inexistente.")
            continue

        encontrado = False
        for viagem in viagens:
            if viagem["caminhao"] == cod_cam and viagem["condutor"] == cod_cond and viagem["data_chegada"] == "":
                viagem["data_chegada"] = input("Data da chegada: ")
                viagem["hora_chegada"] = input("Hora da chegada: ")
                print("Retorno registrado!")
                encontrado = True
                break

        if not encontrado:
            print("Não foi encontrada uma saída em aberto para esse caminhão e condutor.")

    # Consultar caminhão
    elif opcao == '3':
        cod = input("Código do caminhão: ")

        if cod not in cam:
            print("Caminhão inexistente.")
            continue

        encontrado = False
        
        # Checa primeiro se está em rota
        for viagem in viagens:
            if viagem["caminhao"] == cod and viagem["data_chegada"] == "":
                print("\nCaminhão:", cam[viagem["caminhao"]])
                print("Condutor:", cond[viagem["condutor"]])
                print("Saída:", viagem["data_saida"], viagem["hora_saida"])
                print("Situação: Em rota")
                encontrado = True
                break

        # Se não estiver em rota, mostra a última viagem concluída
        if not encontrado:
            for viagem in reversed(viagens): # reversed para pegar a última viagem realizada
                if viagem["caminhao"] == cod:
                    print("\nCaminhão:", cam[viagem["caminhao"]])
                    print("Condutor:", cond[viagem["condutor"]])
                    print("Saída:", viagem["data_saida"], viagem["hora_saida"])
                    print("Chegada:", viagem["data_chegada"], viagem["hora_chegada"])
                    print("Situação: Disponível (Na garagem)")
                    encontrado = True
                    break

        if not encontrado:
            print("Esse caminhão ainda não possui viagens cadastradas.")

    # Listar caminhões
    elif opcao == '4':
        print("\n===== CAMINHÕES =====")
        for codigo, nome in cam.items():
            print(f"{codigo} - {nome}")

    # Listar condutores
    elif opcao == '5':
        print("\n===== CONDUTORES =====")
        for codigo, nome in cond.items():
            print(f"{codigo} - {nome}")

    # Listar retornos por data
    elif opcao == '6':
        data = input("Digite a data: ")
        encontrou = False

        print("\n===== CAMINHÕES QUE RETORNARAM =====")
        for viagem in viagens:
            if viagem["data_chegada"] == data:
                print("Código:", viagem["caminhao"])
                print("Caminhão:", cam[viagem["caminhao"]])
                print("Condutor:", cond[viagem["condutor"]])
                print("Hora da chegada:", viagem["hora_chegada"])
                print()
                encontrou = True

        if not encontrou:
            print("Nenhum caminhão retornou nessa data.")

    # Verificar entregas do dia
    elif opcao == '7':
        data = input("Digite a data: ")
        encontrou = False
        todas = True

        for viagem in viagens:
            if viagem["data_saida"] == data:
                encontrou = True
                if viagem["data_chegada"] == "":
                    todas = False

        if not encontrou:
            print("Nenhum caminhão saiu nessa data.")
        elif todas:
            print("Todas as entregas iniciadas nessa data foram concluídas.")
        else:
            print("Ainda existem caminhões em rota.")

    # Sair
    elif opcao == '0':
        print("\nSistema encerrado.\n")

    # Opção inválida
    else:
        print("Opção inválida!")