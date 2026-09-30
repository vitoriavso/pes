'''10 - Construa uma função que receba uma string como parâmetro e devolva (retorne)
outra string com os caracteres embaralhados. Por exemplo: se função receber a palavra
python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma
aleatória. Padronize sua função que todos os caracteres sejam devolvidos em caixa alta
ou caixa baixa, independentemente de como foram digitados. Para lhe auxiliar nesse
exercício, pesquisa sobre a biblioteca Random do Python.'''

import random

def embaralhar(palavra):
    palavra = palavra.lower()
    caracteres = list(palavra)
    random.shuffle(caracteres)
    return ''.join(caracteres)

palavra = input("Digite uma palavra: ")

resultado = embaralhar(palavra)

print("Palavra embaralhada:", resultado)