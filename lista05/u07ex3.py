'''3 – Codifique um programa com uma função para calcular o volume de um cilindro. Seu
programa principal deve solicitar a altura e o raio do cilindro em metros, chamar a função
e exibir o resultado na tela. '''


from math import pi


def vol_cilindro(altura, raio):
    return pi * (raio ** 2) * altura

h = float(input('Digite a altura do cilindro em metros: '))

r = float(input('Digite o raio do cilindro em metros: '))

print(f'O volume do cilindro é: {vol_cilindro(h, r):.2f} metros cúbicos.')