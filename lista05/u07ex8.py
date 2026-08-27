'''8 - Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada no formato
de string, por exemplo: “15:31”. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para imprimir a saída. A função que faz a conversão deve ter duas
saídas: uma com a hora convertida e outra com “A”, caso seja “A.M.” e “P”, caso seja
“P.M.”. Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar.'''

def converter(horario):
    hora = int(horario[:2])
    minuto = horario[3:]

    if hora == 0:
        hora = 12
        periodo = "A"
    elif hora < 12:
        periodo = "A"
    elif hora == 12:
        periodo = "P"
    else:
        hora = hora - 12
        periodo = "P"

    return hora, minuto, periodo


def imprimir(hora, minuto, periodo):
    print(f"{hora}:{minuto} {periodo}.M.")


while True:
    horario = input("Digite o horário no formato HH:MM: ")

    hora, minuto, periodo = converter(horario)

    imprimir(hora, minuto, periodo)

    continuar = input("Deseja fazer outra conversão? (S/N): ")

    if continuar.upper() != "S":
        break