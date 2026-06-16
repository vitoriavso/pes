'''8 – Suponha que você recebeu a última fatura do seu cartão de crédito no valor de R$
1.000,00 e que você não possa pagá-la. Faça um programa que calcule sua dívida total
com o banco depois de uma quantidade de meses informada durante a execução do 
programa. Considere que a taxa de juros mensal de um cartão de crédito é de 15,30% ao
mês. Fonte da taxa de juros utilizada: https://einvestidor.estadao.com.br/educacaofinanceira/juros-cartao-de-credito-dicas-para-evitar-dividas/
A título de curiosidade, simule sua dívida final no prazo de 2 anos (24 meses).'''

divida_inicial = 1000.0
taxa_juros = 15.3 / 100 
meses = int(input("Informe a quantidade de meses que você não pagará a fatura: "))
divida_final = divida_inicial * (1 + taxa_juros) ** meses
print(f"Sua dívida após {meses} meses será de R$ {divida_final:.2f}")