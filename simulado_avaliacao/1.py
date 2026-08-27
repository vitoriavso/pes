'''1 – Desenvolva um algoritmo que leia um ano e informe se ele é bissexto. Um ano é bissexto quando
é divisível por 400 ou quando é divisível por 4, mas não é divisível por 100.'''

def ano_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

while True:
    year = int(input("Digite um ano que você deseja verificar: "))
    if ano_bissexto(year) == True:
        print(f"O ano {year} é bissexto.")
    else:
        print(f'O ano {year} não é bissexto.')

    continuar = input("Deseja verificar outro ano? (s/n): ")
    if continuar.lower() != 's':
        print('Saindo do programa...')
        break

