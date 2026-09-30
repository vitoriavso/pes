'''3 – Faça um programa que exiba na tela a contagem iniciando no número 1 e indo até um
número informado pelo usuário. Considere que a contagem pode ser até um número
positivo ou até um número negativo.'''

n = int(input('Informe o número: '))

if n < 0:
    for i in range (1, n - 1, -1):
        print (i)
else:
    for i in range (1, n + 1, 1):
        print (i)