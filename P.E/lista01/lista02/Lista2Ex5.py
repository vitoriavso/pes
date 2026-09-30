'''5 – Faça um programa que exiba na tela a tabuada de um número informado pelo
usuário. Vamos supor que o número informado seja o 2, então o programa deve exibir o
seguinte resultado na tela:
Tabuada do número 2
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20'''

x = 1
n = int(input('Informe um número: '))

while x <= 10:
    print ('n x ', x, '=', n * x)
    x = x + 1
