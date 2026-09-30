'''11 – Crie um algoritmo com uma função que retorna um valor em reais escrito por
extenso. Por exemplo, caso seja passado “1.74” como parâmetro para a função, ela deve
retornar: um real e setenta e quatro centavos. Caso seja passado “3251.90”, deve retornar
“três mil duzentos e cinquenta e um reais e noventa centavos”.'''

def numero_por_extenso(numero):
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
    ]

    especiais = [
        "dez", "onze", "doze", "treze", "quatorze",
        "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"
    ]

    dezenas = [
        "", "", "vinte", "trinta", "quarenta",
        "cinquenta", "sessenta", "setenta", "oitenta", "noventa"
    ]

    centenas = [
        "", "cento", "duzentos", "trezentos", "quatrocentos",
        "quinhentos", "seiscentos", "setecentos",
        "oitocentos", "novecentos"
    ]

    def ate_999(n):
        if n == 0:
            return ""

        if n < 10:
            return unidades[n]

        if n < 20:
            return especiais[n - 10]

        if n < 100:
            if n % 10 == 0:
                return dezenas[n // 10]
            return dezenas[n // 10] + " e " + unidades[n % 10]

        if n == 100:
            return "cem"

        if n < 1000:
            if n % 100 == 0:
                return centenas[n // 100]
            return centenas[n // 100] + " e " + ate_999(n % 100)

    valor = float(numero)

    reais = int(valor)
    centavos = round((valor - reais) * 100)

    partes = []

    if reais >= 1000000:
        milhoes = reais // 1000000

        if milhoes == 1:
            partes.append("um milhão")
        else:
            partes.append(ate_999(milhoes) + " milhões")

        reais = reais % 1000000

    if reais >= 1000:
        milhares = reais // 1000

        if milhares == 1:
            partes.append("mil")
        else:
            partes.append(ate_999(milhares) + " mil")

        reais = reais % 1000

    if reais > 0:
        partes.append(ate_999(reais))

    if not partes:
        texto_reais = "zero reais"
    else:
        texto_reais = " ".join(partes)

        if valor == 1:
            texto_reais += " real"
        else:
            texto_reais += " reais"

    if centavos == 1:
        texto_centavos = "um centavo"
    elif centavos > 0:
        texto_centavos = ate_999(centavos) + " centavos"
    else:
        texto_centavos = ""

    if centavos > 0:
        return texto_reais + " e " + texto_centavos

    return texto_reais


valor = input("Digite o valor em reais: ")

print(numero_por_extenso(valor))