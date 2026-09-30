'''9 - Construa uma função que receba uma data no formato DD/MM/AAAA (string) e
devolva uma string com a data por extenso, por exemplo: “doze de agosto de dois mil e
vinte e quatro”. Seu algoritmo deve ser capaz de converter datas entre os anos de 2000 e
2100.'''

def numero_por_extenso(numero):
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
    ]

    especiais = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }

    dezenas = {
        20: "vinte",
        30: "trinta",
        40: "quarenta",
        50: "cinquenta",
        60: "sessenta",
        70: "setenta",
        80: "oitenta",
        90: "noventa"
    }

    if numero < 10:
        return unidades[numero]

    elif numero < 20:
        return especiais[numero]

    elif numero % 10 == 0:
        return dezenas[numero]

    else:
        dezena = numero - numero % 10
        unidade = numero % 10

        return dezenas[dezena] + " e " + unidades[unidade]


def ano_por_extenso(ano):
    if ano == 2000:
        return "dois mil"

    elif ano == 2100:
        return "dois mil e cem"

    else:
        return "dois mil e " + numero_por_extenso(ano - 2000)


def data_por_extenso(data):
    dias = {
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
        20: "vinte",
        21: "vinte e um",
        22: "vinte e dois",
        23: "vinte e três",
        24: "vinte e quatro",
        25: "vinte e cinco",
        26: "vinte e seis",
        27: "vinte e sete",
        28: "vinte e oito",
        29: "vinte e nove",
        30: "trinta",
        31: "trinta e um"
    }

    meses = [
        "janeiro",
        "fevereiro",
        "março",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro"
    ]

    dia, mes, ano = data.split("/")

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if ano < 2000 or ano > 2100:
        return "Ano inválido!"

    if dia < 1 or dia > 31:
        return "Dia inválido!"

    if mes < 1 or mes > 12:
        return "Mês inválido!"

    resultado = (
        dias[dia]
        + " de "
        + meses[mes - 1]
        + " de "
        + ano_por_extenso(ano)
    )

    return resultado


data = input("Digite uma data no formato DD/MM/AAAA: ")

print(data_por_extenso(data))