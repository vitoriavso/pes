'''7 - Desenha moldura. Construa uma função que desenhe um retângulo usando os
caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas,
sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se
valores fora da faixa forem informados, eles devem ser modificados para valores dentro
da faixa de forma elegante.'''


def moldura(linhas=1, colunas=1):
	#Desenha uma moldura com dimensões limitadas ao intervalo [1, 20]
	linhas = max(1, min(20, linhas))
	colunas = max(1, min(20, colunas))

	if linhas == 1:
		print("+" + "-" * (colunas - 2) + "+" if colunas > 1 else "+")
		return

	if colunas == 1:
		print("+\n" + "|\n" * (linhas - 2) + "+")
		return

	borda = "+" + "-" * (colunas - 2) + "+"
	interior = "|" + " " * (colunas - 2) + "|"
	print(borda)
	for _ in range(linhas - 2):
		print(interior)
	print(borda)

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunas: "))

moldura(linhas, colunas)
 