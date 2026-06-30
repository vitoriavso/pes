'''2 – Crie um programa que registrará as notas de um estudante. O programa deve
perguntar ao usuário quantas notas devem ser digitadas e, em seguida, fazer a leitura das
notas e, ao final, exibir todas as notas digitadas na tela.'''

indice = 0
notas = []
qtd = int(input('Quantas notas serão cadastradas?'))

while indice < qtd:
    nota = int(input("Digite a primeira nota:"))
    notas.append(nota)
    indice = indice + 1

print("Notas: ")
for elemento in notas:
    print(elemento)