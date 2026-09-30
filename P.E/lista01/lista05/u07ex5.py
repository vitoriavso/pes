'''5 – Programe um algoritmo com mais algumas funções úteis para a manipulação de listas
numéricas:
a) uma função que receba uma lista e retorne True, caso esteja vazia, ou False, caso
possua um ou mais elementos;
b) uma função que receba uma lista e retorne o maior valor;
c) uma função que receba uma lista e retorne o menor valor;
d) uma função que receba uma lista e retorne o valor médio.
As funções dos itens b, c e d devem retornar -1 caso a lista esteja vazia. No seu
programa principal, crie duas listas (uma vazia e outra com alguns elementos) e teste
(comprove) o funcionamento de cada uma das funções.'''

from minhasdef import soma_lista

def lista_vazia(lista):
    return len(lista) == 0  

def maior_valor(lista):
    if lista_vazia(lista):
        return -1
    return max(lista)

def menor_valor(lista):
    if lista_vazia(lista):
        return -1
    return min(lista)

def valor_medio(lista):
    if lista_vazia(lista):
        return -1
    return soma_lista(lista) / len(lista)

lista1 = []
lista2 = [10, 20, 30, 40, 50]

print(f'\nLista 1 está vazia: {lista_vazia(lista1)}')
print(f'\nLista 2 está vazia: {lista_vazia(lista2)}')
print(f'\nMaior valor na Lista 1: {maior_valor(lista1)}')
print(f'\nMaior valor na Lista 2: {maior_valor(lista2)}')
print(f'\nMenor valor na Lista 1: {menor_valor(lista1)}')
print(f'\nMenor valor na Lista 2: {menor_valor(lista2)}')
print(f'\nValor médio na Lista 1: {valor_medio(lista1)}')
print(f'\nValor médio na Lista 2: {valor_medio(lista2)}\n')