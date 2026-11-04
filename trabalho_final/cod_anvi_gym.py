
from classes_ANVI import Loja
from def_anvi import menu_admin, menu_usuario, menu_contas

#PROGRAMA PRINCIPAL
loja = Loja()

while True:

    print("\n================================")
    print("            ANVI GYM")
    print("       SISTEMA DE VENDAS")
    print("================================")
    print("1 - Fazer login")
    print("2 - Criar conta de usuário")

    if not any(u.tipo == "admin" for u in loja.usuarios):
        print("3 - Configurar primeiro administrador")

    print("0 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        usuario = loja.login()

        if usuario is not None:

            if usuario.tipo == "admin":

                menu_admin(loja, usuario)

            elif usuario.tipo == "user":

                menu_usuario(loja, usuario)

    elif opcao == "2":

        loja.cadastrar_usuario("user")

    elif opcao == "3":

        loja.configurar_primeiro_admin()

    elif opcao == "0":

        print("\nObrigado por utilizar o Anvi Gym!")
        break

    else:

        print("\nOpção inválida!")
