'''4 – Desenvolva um algoritmo com uma função que receba uma lista numérica e retorne o
resultado da soma de todos os elementos dela. Seu programa principal deve solicitar 4
números ao usuário, chamar a função e exibir o resultado da soma na tela.'''

def soma_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


num = []

for i in range(4):
    valor = float(input(f'Digite o {i + 1}º número: '))
    num.append(valor)

print(f'A soma dos números é: {soma_lista(num)}')