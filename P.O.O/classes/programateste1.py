from minhas_classes import Estudante

estudante1 = Estudante()
estudante2 = Estudante()
estudante3 = Estudante()

estudante1.nome = input(" \nDigite o nome do estudante 1:")
estudante1.sobrenome = input("\nDigite o sobrenome do estudante 1: ")
estudante1.idade = int(input("\nDigite a idade do estudante 1: "))
estudante1.cpf = input("\nDigite o CPF do estudante 1: ")

estudante2.nome = input("\nDigite o nome do estudante 2: ")
estudante2.sobrenome = input("\nDigite o sobrenome do estudante 2: ")
estudante2.idade = int(input("\nDigite a idade do estudante 2: "))
estudante2.cpf = input("\nDigite o CPF do estudante 2: ")

estudante3.nome = input("\nDigite o nome do estudante 3: ")
estudante3.sobrenome = input("\nDigite o sobrenome do estudante 3: ")
estudante3.idade = int(input("\nDigite a idade do estudante 3: "))
estudante3.cpf = input("\nDigite o CPF do estudante 3: ")

print('\n', estudante1.nome, 'tem', estudante1.idade, 'anos\n')
print(estudante2.nome, 'tem', estudante2.idade, 'anos\n')
print(estudante3.nome, 'tem', estudante3.idade, 'anos\n')

print('\nApresentações dos estudantes:\n')
print(estudante1.apresentar())
print(estudante2.apresentar())
print(estudante3.apresentar())
