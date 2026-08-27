'''4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
significados como valores. Inicie com:
"apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
situação difícil, ou usar de meios extremos e exagerados"
Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
não encontrada”.'''

dicionario = {
    "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados"
}

for i in range(4):
    palavra = input(f"Digite a {i+1}ª palavra: ")
    significado = input(f"Digite o significado de '{palavra}': ")
    dicionario[palavra] = significado

while True:
    consulta = input("\nDigite a palavra que deseja consultar: ")

    if consulta in dicionario:
        print(f"Significado de '{consulta}': {dicionario[consulta]}")
    else:
        print("Palavra não encontrada")

    continuar = input("Deseja consultar outra palavra? (s/n): ")
    if continuar.lower() != 's':
        print('Saindo do programa...')
        break