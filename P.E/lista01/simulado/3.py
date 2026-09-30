'''3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
exiba o valor a ser pago.'''

produto = input("Digite o produto que vocÊ deseja comprar: ")
preco = float(input('Digite o preço do produto: '))
qtd = int(input('Qual a quantidade do produto que você vai comprar? '))

tot = preco * qtd

if tot == 100 or tot > 100:
    tot = tot * 1.10
    print(f'Você ganhou um desconto de 10% na sua compra! O total a ser pago é de R${tot:.2f}')
else:
    print(f'O total a ser pago é de R${tot:.2f}')