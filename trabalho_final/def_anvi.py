
def menu_admin(loja, usuario):

    while True:

        print("\n================================")
        print("        ANVI GYM - ADMIN")
        print(f"        Olá, {usuario.nome}")
        print("================================")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar estoque")
        print("4 - Gerenciar contas")
        print("5 - Relatórios de vendas")
        print("0 - Fazer logout")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            loja.cadastrar_produto()

        elif opcao == "2":

            loja.listar_produtos()

        elif opcao == "3":

            loja.atualizar_estoque()

        elif opcao == "4":

            menu_contas(loja)

        elif opcao == "5":

            loja.relatorios_vendas()

        elif opcao == "0":

            print("Logout realizado!")
            break

        else:

            print("Opção inválida!")


# MENU DO USUARIO

def menu_usuario(loja, usuario):

    while True:

        print("\n================================")
        print("        ANVI GYM - LOJA")
        print(f"        Olá, {usuario.nome}")
        print("================================")
        print("1 - Visualizar produtos")
        print("2 - Comprar produtos")
        print("3 - Minhas compras")
        print("0 - Fazer logout")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            loja.listar_produtos()

        elif opcao == "2":

            loja.comprar_produto(usuario)

        elif opcao == "3":

            loja.minhas_compras(usuario)

        elif opcao == "0":

            print("Logout realizado!")
            break

        else:

            print("Opção inválida!")

# MENU DE GERENCIAMENTO DE CONTAS


def menu_contas(loja):

    while True:

        print("\n================================")
        print("       GERENCIAR CONTAS")
        print("================================")
        print("1 - Cadastrar administrador")
        print("2 - Cadastrar usuário")
        print("3 - Listar todas as contas")
        print("0 - Voltar")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            loja.cadastrar_usuario("admin")

        elif opcao == "2":

            loja.cadastrar_usuario("user")

        elif opcao == "3":

            loja.listar_usuarios()

        elif opcao == "0":

            break

        else:

            print("Opção inválida!")

