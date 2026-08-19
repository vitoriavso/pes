'''1 – Crie um programa com uma função para calcular a média aritmética simples entre 3
notas. Seu programa deve solicitar 3 notas, chamar a função e exibir o resultado na tela.'''


def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


v1 = float(input('Digite um valor para v1: '))
v2 = float(input('Digite um valor para v2: '))
v3 = float(input('Digite um valor para v3: '))
resultado = calcular_media(v1, v2, v3)
print(f'Resultado: {resultado:.2f}')
