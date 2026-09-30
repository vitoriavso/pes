'''Elabore um algoritmo que leia as notas de 10 alunos e armazene-as em uma lista.

Aceite apenas notas entre 0 e 10. Caso o usuário informe uma nota inválida, solicite novamente a nota.

Ao final, exiba:

Todas as notas cadastradas;
A maior nota;
A menor nota;
A média da turma.'''
notas = []

for i in range(10):

    nota = float(input('Digite a nota do aluno: '))

    while nota < 0 or nota > 10:
        print('Nota inválida. Digite uma nota entre 0 e 10.')
        nota = float(input('Digite a nota do aluno: '))

    notas.append(nota)

# Todas as notas
print('\nNotas cadastradas:')

indice = 0

for nota in notas:
    print(f'Nota do aluno {indice + 1}: {nota}')
    indice += 1

# Maior nota
maior = notas[0]

for nota in notas:
    if nota > maior:
        maior = nota

# Menor nota
menor = notas[0]

for nota in notas:
    if nota < menor:
        menor = nota

# Média
soma = 0

for nota in notas:
    soma += nota

media = soma / 10

print(f'\nMaior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Média da turma: {media:.2f}')