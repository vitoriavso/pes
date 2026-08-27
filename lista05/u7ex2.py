'''2 – Elabore um algoritmo com uma função que retorne se um dado número é par ou
ímpar. Seu programa deve solicitar um número ao usuário, chamar a função e exibir o
resultado na tela.'''

def par_ou_impar(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'ímpar'

numero = int(input('Digite um número: '))
print(f'O número {numero} é {par_ou_impar(numero)}.')