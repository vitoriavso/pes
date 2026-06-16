'''1 – Solicite o valor total de uma compra. Se o valor for maior ou igual a 100, exiba "Você
ganhou um cupom de desconto!". Caso contrário, exiba "Continue comprando para
ganhar um cupom de desconto!".'''

valor_tot = float(input('Qual é o valor total da compra?'))
if valor_tot >= 100:
    print ('Você ganhou um cupom de desconto!')
else:
    print('Continue comprando para ganhar um cupom de desconto!')