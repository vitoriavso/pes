'''2 - Exercício 2: Computador e CPU (1..1).
Objetivo: Implementar um relacionamento obrigatório (Composição).
Classes: CPU e Computador.
Regras:
A classe CPU deve ter atributos fabricante (ex: "Intel") e modelo (ex: "i7-12700K").
• A classe Computador deve ter um atributo tipo (ex: "Desktop" ou "Notebook").
• Um Computador deve ter exatamente uma CPU para ser criado (1..1).
• O __init__ do Computador deve receber os dados necessários para criar sua
própria instância de CPU. O atributo computador.cpu nunca pode ser None.
Comprove o funcionamento da sua implementação no programa principal.'''

from minhasclasses7 import Computador

print("--- Criando o computador ---")
tipo = input("Digite o tipo do computador (Desktop/Notebook): ")
fabricante_cpu = input("Digite o fabricante da CPU: ")
modelo_cpu = input("Digite o modelo da CPU: ")
computador = Computador(tipo, fabricante_cpu, modelo_cpu)

print(f"Computador criado: {computador}")