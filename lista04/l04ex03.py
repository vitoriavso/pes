'''3 – Utilizando como base o exercício anterior, faça com seu programa exiba uma saída
formatada da forma exibida abaixo (abaixo é utilizado com exemplo com 3 notas). Você
deve fazer isso de duas formas: com while e com for.
Exibição com while:
Nota: 9.0
Nota: 7.5
Nota: 8.0
Exibição com for:
Nota: 9.0
Nota: 7.5
Nota: 8.0'''

# percorrendo com o for
'''indice = 0
notas = []
qtd = int(input('Quantas notas serão cadastradas? '))

while indice < qtd:
    nota = float(input("Digite a primeira nota: "))
    notas.append(nota)
    indice = indice + 1

for elemento in notas:
    print('Nota: ', elemento)'''

# percorrendo com o while

indice = 0
notas = []
qtd = int(input('Quantas notas serão cadastradas? '))

while indice < qtd:
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    indice = indice + 1

quantidade = len(notas)
indice = 0
while indice < quantidade:
 print("Nota: ", notas[indice])
 indice = indice + 1