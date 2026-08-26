'''2 – Elabore um algoritmo que leia 15 números de uma cartela de bingo e armazene-os em uma lista.
Aceite apenas números entre 1 e 75 e não permita valores repetidos. Ao final, ordene a lista e
exiba os números do menor para o maior.'''

bingo = []*15
indice = 0
while indice < 15:
    num = int(input('Digite um numero de 1 à 75 para completar sua tabela de bingo: '))
    if num == 0 or num > 75 or num < 1:
        print('Esse número não é válido.')
        continue
    if num in bingo:
        print('Esse número ja está na tabela')
    else:
        bingo.append(num)
        indice = indice + 1

print('\nSua tabela está completa!')
print ('\nAqui etá os valores ordenados em ordem crescente: ')

bingo = sorted(bingo)

print(bingo)