from minhas_classes import Professor

professor1 = Professor()
professor2 = Professor()

professor1.nome = input("Digite o nome do professor 1: ")
professor1.sobrenome = input("Digite o sobrenome do professor 1: ")
professor1.disciplina = input("Digite a disciplina do professor 1: ")

professor2.nome = input("Digite o nome do professor 2: ")
professor2.sobrenome = input("Digite o sobrenome do professor 2: ")
professor2.disciplina = input("Digite a disciplina do professor 2: ")

print('\n', professor1.apresentar())
print('\n', professor2.apresentar())