'''1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
professores já cadastrados no sistema de uso dos laboratórios.
O sistema deve possuir:

• Um cadastro completo de professores (adicionar, alterar, excluir e listar) que
associe o código do professor ao seu nome, alguns professores já devem ser précadastrados, veja a lista abaixo;

• Um cadastro completo dos acessos dos professores aos laboratórios (adicionar,
alterar, excluir e listar), serão utilizados 6 laboratórios com as nomenclaturas
Lab102, Lab103, Lab104, Lab105, Lab106, Lab107 – os laboratórios são fixos no
sistema, o que pode ser alterado são os acessos, alguns professores já devem
ser pré-cadastrados nos laboratórios, veja a outra lista abaixo (para facilitar a
implementação, sugere-se que os laboratórios sejam associados ao código do
professor e não ao seu nome);

• Teste de acesso ao laboratório: deve ser possível informar o nome de um
laboratório e um código de professor para verificar se o acesso é permitido ou não
(por exemplo, nesse teste deveria ser possível escolher o Lab103 e informar o
código de professor 002, nesse caso, o sistema deve negar o acesso).
Pré-cadastro de Professores (códigos x nomes)
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
Pré-cadastro de Acessos (laboratório x professor)
• Lab102 – Prof Ignácio, Prof Thiago Paes, Profª Ryan, Prof André, Profª
Fabiana;
• Lab103 – Prof Alberto;
• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;
• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof
João Eduardo.'''

# Cadastro de Professores

profs = {
    "001": "Prof Thiago Paes",
    "002": "Prof Schalata",
    "003": "Prof Ignácio",
    "004": "Prof Ryan",
    "005": "Prof André",
    "006": "Profª Fabiana",
    "007": "Prof Alberto",
    "008": "Prof Juliano",
    "009": "Prof Thiago Waltrik",
    "010": "Prof João Eduardo"
}

# Listas dos laboratórios

lab102 = ["003", "001", "004", "005", "006"]
lab103 = ["007"]
lab104 = ["004", "008", "002", "005"]
lab105 = ["003", "007", "009", "001"]
lab106 = ["002", "003", "009", "001"]
lab107 = ["005", "002", "009", "001", "010"]

opcao = -1

while opcao != 0:

    print("\n====== SISTEMA DE LABORATÓRIOS ======")
    print("1 - Cadastro de laboratórios")
    print("2 - Cadastro de professores")
    print("3 - Teste de acesso por crachá")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")


    # Cadastro de laboratórios

    if opcao == '1':

        print("\n====== LABORATÓRIOS ======")
        print("1 - Cadastrar laboratórios")
        print("2 - Listar laboratórios")
        print("3 - Alterar acesso ao laboratório")
        print("4 - Remover acesso de professores em laboratórios")

        op = input("Escolha uma opção: ")


        # Cadastro automático dos laboratórios

        if op == '1':

            lab102 = ["003", "001", "004", "005", "006"]
            lab103 = ["007"]
            lab104 = ["004", "008", "002", "005"]
            lab105 = ["003", "007", "009", "001"]
            lab106 = ["002", "003", "009", "001"]
            lab107 = ["005", "002", "009", "001", "010"]

            print("\nLaboratórios cadastrados com sucesso!")


        # Listar laboratório

        elif op == '2':

            lab = input("\nDigite o laboratório (Lab102 até Lab107): ")

            if lab == "Lab102":

                print("\nProfessores que possuem acesso ao Lab102:")

                for codigo in lab102:
                    print(codigo, "-", profs[codigo])


            elif lab == "Lab103":

                print("\nProfessores que possuem acesso ao Lab103:")

                for codigo in lab103:
                    print(codigo, "-", profs[codigo])


            elif lab == "Lab104":

                print("\nProfessores que possuem acesso ao Lab104:")

                for codigo in lab104:
                    print(codigo, "-", profs[codigo])


            elif lab == "Lab105":

                print("\nProfessores que possuem acesso ao Lab105:")

                for codigo in lab105:
                    print(codigo, "-", profs[codigo])


            elif lab == "Lab106":

                print("\nProfessores que possuem acesso ao Lab106:")

                for codigo in lab106:
                    print(codigo, "-", profs[codigo])


            elif lab == "Lab107":

                print("\nProfessores que possuem acesso ao Lab107:")

                for codigo in lab107:
                    print(codigo, "-", profs[codigo])


            else:

                print("Laboratório inexistente!")


        # Alterar acesso

        elif op == '3':

            lab = input("\nDigite o laboratório (Lab102 até Lab107): ")
            cracha = input("Digite o código do crachá: ")

            if cracha not in profs:

                print("Professor não encontrado.")

            elif lab == "Lab102":

                if cracha not in lab102:
                    lab102.append(cracha)
                    print("Acesso adicionado ao Lab102.")
                else:
                    print("O professor já possui acesso ao Lab102.")


            elif lab == "Lab103":

                if cracha not in lab103:
                    lab103.append(cracha)
                    print("Acesso adicionado ao Lab103.")
                else:
                    print("O professor já possui acesso ao Lab103.")


            elif lab == "Lab104":

                if cracha not in lab104:
                    lab104.append(cracha)
                    print("Acesso adicionado ao Lab104.")
                else:
                    print("O professor já possui acesso ao Lab104.")


            elif lab == "Lab105":

                if cracha not in lab105:
                    lab105.append(cracha)
                    print("Acesso adicionado ao Lab105.")
                else:
                    print("O professor já possui acesso ao Lab105.")


            elif lab == "Lab106":

                if cracha not in lab106:
                    lab106.append(cracha)
                    print("Acesso adicionado ao Lab106.")
                else:
                    print("O professor já possui acesso ao Lab106.")


            elif lab == "Lab107":

                if cracha not in lab107:
                    lab107.append(cracha)
                    print("Acesso adicionado ao Lab107.")
                else:
                    print("O professor já possui acesso ao Lab107.")


            else:

                print("Laboratório inexistente!")


        # Remover acesso

        elif op == '4':

            lab = input("\nDigite o laboratório (Lab102 até Lab107): ")
            cracha = input("Digite o código do crachá: ")


            if lab == "Lab102":

                if cracha in lab102:
                    lab102.remove(cracha)
                    print("Acesso removido do Lab102.")
                else:
                    print("O professor não possui acesso ao Lab102.")


            elif lab == "Lab103":

                if cracha in lab103:
                    lab103.remove(cracha)
                    print("Acesso removido do Lab103.")
                else:
                    print("O professor não possui acesso ao Lab103.")


            elif lab == "Lab104":

                if cracha in lab104:
                    lab104.remove(cracha)
                    print("Acesso removido do Lab104.")
                else:
                    print("O professor não possui acesso ao Lab104.")


            elif lab == "Lab105":

                if cracha in lab105:
                    lab105.remove(cracha)
                    print("Acesso removido do Lab105.")
                else:
                    print("O professor não possui acesso ao Lab105.")


            elif lab == "Lab106":

                if cracha in lab106:
                    lab106.remove(cracha)
                    print("Acesso removido do Lab106.")
                else:
                    print("O professor não possui acesso ao Lab106.")


            elif lab == "Lab107":

                if cracha in lab107:
                    lab107.remove(cracha)
                    print("Acesso removido do Lab107.")
                else:
                    print("O professor não possui acesso ao Lab107.")


            else:

                print("Laboratório inexistente!")


        else:

            print("\nOpção inválida!")


    # Cadastro de professores

    elif opcao == '2':

        print("\n====== CADASTRO DE PROFESSORES ======")
        print("1 - Cadastrar professores existentes")
        print("2 - Cadastrar novo professor")
        print("3 - Listar professores")
        print("4 - Alterar professor")
        print("5 - Excluir professor")

        op = input("Escolha uma opção: ")


        # Cadastro automático

        if op == '1':

            print("\nProfessores cadastrados com sucesso!")


        # Cadastrar novo professor

        elif op == '2':

            print("\nCadastro de Novo Professor\n")

            encontrou = False

            while encontrou == False:

                codigo = input("Digite o código do professor: ")

                if codigo in profs:

                    print("O código do professor já está em uso.")

                else:

                    nome = input("Digite o nome do professor: ")

                    profs[codigo] = nome

                    print("Professor cadastrado com sucesso!")

                    encontrou = True


        # Listar professores

        elif op == '3':

            print("\n====== LISTAGEM DE PROFESSORES ======\n")

            for codigo, nome in profs.items():

                print(codigo, "-", nome)


        # Alterar professor

        elif op == '4':

            print("\n====== ALTERAR PROFESSOR ======\n")
            print("1 - Alterar nome do professor")
            print("2 - Alterar código do professor")

            op = input("Escolha uma opção: ")


            if op == '1':

                cod = input("Digite o código do professor que deseja alterar o nome: ")

                if cod in profs:

                    novo_nome = input("Digite o novo nome do professor: ")

                    profs[cod] = novo_nome

                    print("Professor alterado com sucesso!")

                else:

                    print("Professor não encontrado.")


            elif op == '2':

                cod = input("Digite o código do professor que deseja alterar o código: ")

                if cod in profs:

                    novo_cod = input("Digite o novo código do professor: ")

                    if novo_cod not in profs:

                        profs[novo_cod] = profs[cod]

                        del profs[cod]

                        print("Código do professor alterado com sucesso!")

                    else:

                        print("O novo código já está em uso.")

                else:

                    print("Professor não encontrado.")


            else:

                print("Opção inválida!")


        # Excluir professor

        elif op == '5':

            print('\n Excluir Professor\n')

            cod = input('Digite o código do professor que deseja excluir: ')

            if cod in profs:

                possui_acesso = False

                if cod in lab102:
                    possui_acesso = True

                if cod in lab103:
                    possui_acesso = True

                if cod in lab104:
                    possui_acesso = True

                if cod in lab105:
                    possui_acesso = True

                if cod in lab106:
                    possui_acesso = True

                if cod in lab107:
                    possui_acesso = True


                if possui_acesso:

                    resposta = input("O professor possui acesso a um ou mais laboratórios. Deseja excluir mesmo assim? (s/n): ")

                    if resposta == 's':

                        if cod in lab102:
                            lab102.remove(cod)

                        if cod in lab103:
                            lab103.remove(cod)

                        if cod in lab104:
                            lab104.remove(cod)

                        if cod in lab105:
                            lab105.remove(cod)

                        if cod in lab106:
                            lab106.remove(cod)

                        if cod in lab107:
                            lab107.remove(cod)

                        del profs[cod]

                        print("Professor excluído com sucesso!")
                        print("Os acessos aos laboratórios também foram removidos.")

                    else:

                        print("Exclusão cancelada.")


                else:

                    del profs[cod]

                    print("Professor excluído com sucesso!")

            else:

                print("Professor não encontrado.")


        else:

            print("\nOpção inválida!")


    # Teste de acesso

    elif opcao == '3':

        print("\n====== TESTE DE ACESSO ======\n")

        lab = input("Digite o laboratório (Lab102 até Lab107): ")
        cracha = input("Digite o código do crachá: ")

        autorizado = False


        if lab == "Lab102":

            if cracha in lab102:
                autorizado = True


        elif lab == "Lab103":

            if cracha in lab103:
                autorizado = True


        elif lab == "Lab104":

            if cracha in lab104:
                autorizado = True


        elif lab == "Lab105":

            if cracha in lab105:
                autorizado = True


        elif lab == "Lab106":

            if cracha in lab106:
                autorizado = True


        elif lab == "Lab107":

            if cracha in lab107:
                autorizado = True


        else:

            print("Laboratório inexistente!")


        if lab == "Lab102" or lab == "Lab103" or lab == "Lab104" or lab == "Lab105" or lab == "Lab106" or lab == "Lab107":

            if cracha not in profs:

                print("\nCrachá não cadastrado.")

            elif autorizado:

                print("\nAcesso liberado!")
                print("Professor:", profs[cracha])
                print("Bem-vindo ao", lab)

            else:

                print("\nAcesso NEGADO!")


    # Sair

    elif opcao == '0':

        print("\nSistema encerrado.")
        break

    else:

        print("\nOpção inválida!")