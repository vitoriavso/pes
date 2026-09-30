def numero_por_extenso(numero):
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
    ]

    especiais = {
        10: "dez", 11: "onze", 12: "doze", 13: "treze",
        14: "quatorze", 15: "quinze", 16: "dezesseis",
        17: "dezessete", 18: "dezoito", 19: "dezenove"
    }

    dezenas = [
        "", "", "vinte", "trinta", "quarenta",
        "cinquenta", "sessenta", "setenta",
        "oitenta", "noventa"
    ]

    centenas = [
        "", "cento", "duzentos", "trezentos", "quatrocentos",
        "quinhentos", "seiscentos", "setecentos",
        "oitocentos", "novecentos"
    ]

    def por_extenso(n):
        if n < 10:
            return unidades[n]

        if n < 20:
            return especiais[n]

        if n < 100:
            dezena = n // 10
            unidade = n % 10

            if unidade == 0:
                return dezenas[dezena]

            return dezenas[dezena] + " e " + unidades[unidade]

        if n < 1000:
            centena = n // 100
            resto = n % 100

            if n == 100:
                return "cem"

            if resto == 0:
                return centenas[centena]

            return centenas[centena] + " e " + por_extenso(resto)

        if n < 1000000:
            milhar = n // 1000
            resto = n % 1000

            if milhar == 1:
                resultado = "mil"
            else:
                resultado = por_extenso(milhar) + " mil"

            if resto > 0:
                if resto < 100:
                    resultado += " e " + por_extenso(resto)
                else:
                    resultado += " " + por_extenso(resto)

            return resultado

    reais = int(numero)
    centavos = round((numero - reais) * 100)

    resultado = por_extenso(reais)

    if reais == 1:
        resultado += " real"
    else:
        resultado += " reais"

    if centavos > 0:
        resultado += " e " + por_extenso(centavos)

        if centavos == 1:
            resultado += " centavo"
        else:
            resultado += " centavos"

    return resultado


valor = float(input("Digite o valor em reais: R$ "))

print(numero_por_extenso(valor))
