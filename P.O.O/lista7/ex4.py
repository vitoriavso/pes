'''4 - Exercício: Funcionario e ContratoDeTrabalho (1..1).
Objetivo: Modelar um 1..1 onde a "parte" (Contrato) é obrigatória e contém a lógica de
cálculo que o "todo" (Funcionario) utiliza.
Classes: ContratoDeTrabalho e Funcionario.
Regras:
• A classe ContratoDeTrabalho deve ter salario_bruto (float) e percentual_impostos
(float, ex: 0.11 para 11% de INSS).
• O ContratoDeTrabalho deve ter um método chamado valor_impostos que calcula e
retorna o valor exato do desconto (ex: salario_bruto * percentual_impostos).
• A classe Funcionario deve ter nome e cargo.
• Um Funcionario deve ter exatamente um ContratoDeTrabalho para ser criado
(1..1).
• O __init__ do Funcionario deve receber nome, cargo, e também o salario_bruto e o
percentual_impostos necessários para criar sua própria instância de
ContratoDeTrabalho (Composição). O atributo funcionario.contrato nunca pode ser
None.
• Crie um método chamado salario_liquido na classe Funcionario. Este método deve:
◦ Acessar o salario_bruto do seu contrato.
◦ Acessar o valor_impostos calculado pelo seu contrato.
◦ Retornar o salario_bruto menos o valor_impostos.
Seu programa principal deve ter um menu interativo onde se possa testar todos os
métodos de um objeto do tipo Funcionario. Faça, também, o Diagrama de Classes da sua
implementação final.'''

from minhasclasses7 import Funcionario, ContratoDeTrabalho

# programa principal

funcionarios = []

print("\n\n=== SISTEMA DE FUNCIONÁRIOS ===")
print("Sistema iniciado!\n")

while True:
    print("\n\n=== MENU PRINCIPAL ===")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Consultar funcionário")
    print("4 - Calcular salário líquido")
    print("5 - Excluir funcionário")
    print("6 - Sair\n\n")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n=== CADASTRO DE FUNCIONÁRIO ===")

        nome = input("Digite o nome: ")
        cargo = input("Digite o cargo: ")

        salario_bruto = float(
            input("Digite o salário bruto: R$ ")
        )

        percentual_impostos = float(
            input("Digite o percentual de impostos (ex: 0.11 para 11%): ")
        )

        funcionario = Funcionario(
            nome, cargo, salario_bruto, percentual_impostos
        )

        funcionarios.append(funcionario)

        print("Funcionário cadastrado com sucesso!")

    elif opcao == "2":
        print("\n=== FUNCIONÁRIOS CADASTRADOS ===")

        if len(funcionarios) == 0:
            print("Nenhum funcionário cadastrado.")
        else:
            for funcionario in funcionarios:
                print("\nNome:", funcionario.nome)
                print("Cargo:", funcionario.cargo)
                print(
                    f"Salário bruto: R$ "
                    f"{funcionario.contrato.salario_bruto:.2f}"
                )

    elif opcao == "3":
        nome_busca = input("Digite o nome do funcionário: ")

        encontrado = False

        for funcionario in funcionarios:
            if funcionario.nome.lower() == nome_busca.lower():
                print("\n=== DADOS DO FUNCIONÁRIO ===")
                print("Nome:", funcionario.nome)
                print("Cargo:", funcionario.cargo)

                print(
                    f"Salário bruto: R$ "
                    f"{funcionario.contrato.salario_bruto:.2f}"
                )

                print(
                    f"Percentual de impostos: "
                    f"{funcionario.contrato.percentual_impostos * 100:.2f}%"
                )

                print(
                    f"Valor dos impostos: R$ "
                    f"{funcionario.contrato.valor_impostos():.2f}"
                )

                print(
                    f"Salário líquido: R$ "
                    f"{funcionario.salario_liquido():.2f}"
                )

                encontrado = True

        if not encontrado:
            print("Funcionário não encontrado!")

    elif opcao == "4":
        nome_busca = input("Digite o nome do funcionário: ")

        encontrado = False

        for funcionario in funcionarios:
            if funcionario.nome.lower() == nome_busca.lower():
                impostos = funcionario.contrato.valor_impostos()
                liquido = funcionario.salario_liquido()

                print("\n=== CÁLCULO SALARIAL ===")
                print("Funcionário:", funcionario.nome)

                print(
                    f"Salário bruto: R$ "
                    f"{funcionario.contrato.salario_bruto:.2f}"
                )

                print(f"Desconto de impostos: R$ {impostos:.2f}")
                print(f"Salário líquido: R$ {liquido:.2f}")

                encontrado = True

        if not encontrado:
            print("Funcionário não encontrado!")

    elif opcao == "5":
        nome_busca = input("Digite o nome do funcionário a excluir: ")

        encontrado = False

        for funcionario in funcionarios:
            if funcionario.nome.lower() == nome_busca.lower():
                funcionarios.remove(funcionario)
                print("Funcionário excluído com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Funcionário não encontrado!")

    elif opcao == "6":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")