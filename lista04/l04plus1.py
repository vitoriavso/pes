'''1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
professores já cadastrados no sistema de uso dos laboratórios.

Implemente um algoritmo de acordo com os requisitos listados abaixo:
A – Serão utilizados 6 laboratórios com as nomenclaturas Lab102, Lab103, Lab104,
Lab105, Lab106, Lab107.

B – Os professores autorizados de acordo com cada laboratório:
• Lab102 – Prof Ignácio, Prof Thiago Paes, Prof Ryan, Prof André, Profª
Fabiana;
• Lab103 – Prof Alberto;
• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;
• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof
João Eduardo.

C – O programa deverá ter uma opção para cadastrar as listas por laboratório e a
lista de professores. Deverá ter opção de imprimir todos os cadastros de cada laboratório,
bem como a lista de professores com seu código de crachá.

D - O sistema de identificação de liberação da porta será feito através do fecho
eletrônico através do Crachá do Servidor, conforme a tabela de crachás abaixo. Vamos
simular que a autorização se dará por meio do teclado dos dispositivos na porta. Você
deve criar no seu programa, uma chamada que permita digitar o código do crachá.

Cadastro de Professores
001 – Prof Thiago Paes
002 – Prof Schalata
003 – Prof Ignácio
004 – Prof Ryan
005 – Prof André
006 – Profª Fabiana
007 – Prof Alberto
008 – Prof Juliano
009 – Prof Thiago Waltrik
010 – Prof João Eduardo

Observação: Faça com que seu algoritmo “converse” com o usuário e que seja claro
na troca de mensagens.'''

# Cadastro de Professores
professores = [
    ["001", "Prof Thiago Paes"],
    ["002", "Prof Schalata"],
    ["003", "Prof Ignácio"],
    ["004", "Prof Ryan"],
    ["005", "Prof André"],
    ["006", "Profª Fabiana"],
    ["007", "Prof Alberto"],
    ["008", "Prof Juliano"],
    ["009", "Prof Thiago Waltrik"],
    ["010", "Prof João Eduardo"]
]

# Listas dos laboratórios (inicialmente vazias)
lab102 = []
lab103 = []
lab104 = []
lab105 = []
lab106 = []
lab107 = []

opcao = -1

while opcao != 0:

    print("\n====== SISTEMA DE LABORATÓRIOS ======")
    print("1 - Cadastrar listas dos laboratórios")
    print("2 - Mostrar laboratórios")
    print("3 - Mostrar professores")
    print("4 - Liberar porta por crachá")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")


    if opcao == '1':

        lab102 = ["003", "001", "004", "005", "006"]
        lab103 = ["007"]
        lab104 = ["004", "008", "002", "005"]
        lab105 = ["003", "007", "009", "001"]
        lab106 = ["002", "003", "009", "001"]
        lab107 = ["005", "002", "009", "001", "010"]

        print("\nLaboratórios cadastrados com sucesso!")

    elif opcao == '2':

        print("\nLab102:", lab102)
        print("Lab103:", lab103)
        print("Lab104:", lab104)
        print("Lab105:", lab105)
        print("Lab106:", lab106)
        print("Lab107:", lab107)

    elif opcao == '3':

        print("\nCadastro de Professores\n")

        for professor in professores:
            print(professor[0], "-", professor[1])


    elif opcao == '4':

        laboratorio = input("\nDigite o laboratório (Lab102 até Lab107): ")
        cracha = input("Digite o código do crachá: ")

        autorizado = False

        if laboratorio == "Lab102":
            if cracha in lab102:
                autorizado = True

        elif laboratorio == "Lab103":
            if cracha in lab103:
                autorizado = True

        elif laboratorio == "Lab104":
            if cracha in lab104:
                autorizado = True

        elif laboratorio == "Lab105":
            if cracha in lab105:
                autorizado = True

        elif laboratorio == "Lab106":
            if cracha in lab106:
                autorizado = True

        elif laboratorio == "Lab107":
            if cracha in lab107:
                autorizado = True

        else:
            print("Laboratório inexistente!")

        if autorizado:

            nome = ""

            for professor in professores:
                if professor[0] == cracha:
                    nome = professor[1]

            print("\nAcesso liberado!")
            print("Professor:", nome)
            print("Bem-vindo ao", laboratorio)

        elif laboratorio == "Lab102" or laboratorio == "Lab103" or laboratorio == "Lab104" or laboratorio == "Lab105" or laboratorio == "Lab106" or laboratorio == "Lab107":
            print("\nAcesso NEGADO!")

    elif opcao == '0':
        print("\nSistema encerrado.")
        break

    else:
        print("\nOpção inválida!")

