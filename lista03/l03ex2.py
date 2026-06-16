'''2 – Crie um programa que leia 4 notas de um(a) determinado(a) estudante. Após a leitura
de todas notas, exiba a média aritmética simples e a situação final (aprovado(a) ou
reprovado(a)).'''

notas = [0] * 4

notas[0] = float(input('Primeira nota: '))
notas[1] = float(input('Segunda nota: '))
notas[2] = float(input('Terceira nota: '))
notas[3] = float(input('Quarta nota: '))

soma =0

for elemento in notas:
    soma = soma + elemento
    media = soma / 4
    
print('a média do estudande foi: ', media, 'então ele está ')

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')

