'''9 – Considere que você deseja fazer uma reserva mensal, em dinheiro, para a compra de
um determinado presente para você mesmo(a). Considere que todo mês você depositará,
em uma poupança no banco, um mesmo valor em reais. Faça um programa que leia o
valor que será depositado mensalmente e exiba na tela o valor acumulado mês a mês
durante 24 meses. Considere que a taxa de juros de uma poupança é 0,5% ao mês, que
a poupança não possui nenhum saldo inicial. Você pode utilizar uma calculadora de juros
compostos para validar o cálculo do seu algoritmo, por exemplo o site:
https://www.idinheiro.com.br/calculadoras/calculadora-juros-compostos/'''

reserva = float(input('Quantos reais você gostaria de guardar por mês? '))
taxa = 0.5 / 100 
qtd_mes = 24
valor_acumulado = 0

for mes in range(1, qtd_mes + 1):
    valor_acumulado = (valor_acumulado * (1 + taxa)) + reserva
    print(f'Mês {mes}: R$ {valor_acumulado:.2f}')