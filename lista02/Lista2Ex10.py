'''10 - Escreva um programa que leia números inteiros do teclado. O programa deve ler os
números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de
números digitados, assim como a soma e a média aritmética.'''
# Inicializa variáveis
contador = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro (0 para parar): "))
    
    if numero == 0:
        break  
    
    soma += numero   
    contador += 1   


if contador > 0:
    media = soma / contador
else:
    media = 0

# Exibe os resultados
print(f"Quantidade de números digitados: {contador}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}")