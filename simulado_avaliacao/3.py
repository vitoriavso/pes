'''3 – Faça um algoritmo que leia o preço de um produto e a quantidade comprada. Calcule o total
da compra e, caso ele seja maior ou igual a R$ 100,00, aplique um desconto de 10%. Ao final,
exiba o valor a ser pago.'''

preco = (float(input("Digite o preço do produto: R$ ")))
quantidade = (int(input("Digite a quantidade comprada: ")))

total = preco * quantidade
if total >= 100:
    total = total * 0.90  # Aplica 10% de desconto

print(f"O valor total a ser pago é: R$ {total:.2f}")