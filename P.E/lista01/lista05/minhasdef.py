def Bom_Dia(nome):
    print('Oi, eu sou uma função que diz...')
    print(f'Bom dia, {nome}!')


'''
n = input('Qual o seu nome?')
Bom_Dia(n)
'''


#soma sem return
def soma(a, b):
    print('A soma dos valores é: ', a+b)
    
'''v1 =  int(input('Digite um número para o valor 1: '))
v2 =  int(input('Digite um número para o valor 2: '))

soma(v1, v2)'''



#soma com return
def somacr(a, b):
    return a+b

'''v1 = int(input('Digite um valor para v1: '))
v2 = int(input('Digite um valor para v2: '))
resultado = somacr(v1, v2)
print('Resultado: ', resultado)'''



#somar valores de uma lista
def soma_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


#calcular tempo total
def tempo_total(horas, minutos):
    return horas * 60 + minutos 