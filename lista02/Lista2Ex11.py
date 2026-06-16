'''11 – Faça um programa para controlar o caixa de uma cantina. Seu programa deve
solicitar ao usuário o código do produto pedido e a quantidade comprada. Suponha que
para cada compra, apenas um tipo de produto possa ser comprado. O programa deve ser
interrompido caso o usuário digite 0. Para cada compra, seu programa deve exibir na tela
o nome do produto comprado e o valor total da compra. Ao final do programa, deve exibir
o valor total acumulado no caixa. Utilize a seguinte tabela de produtos como referência:'''
# Tabela de produtos (código: [nome, preço])
produtos = {
    1: ["Suco", 6.00],
    2: ["Pão de queijo", 3.00],
    3: ["Pastel", 7.00],
    4: ["Salada de frutas", 9.00],
    5: ["Café com leite", 3.50],
    6: ["Cappuccino", 4.50],
    7: ["Iogurte", 6.50],
    8: ["Água", 2.50]
}

total_caixa = 0

print("Bem-vindo à cantina! Digite 0 para encerrar as compras.")

while True:
    codigo = int(input("Digite o código do produto: "))
    
    if codigo == 0:
        break  # encerra o programa
    
    if codigo not in produtos:
        print("Código inválido! Tente novamente.")
        continue
    
    quantidade = int(input(f"Digite a quantidade de {produtos[codigo][0]}: "))
    
    valor_compra = produtos[codigo][1] * quantidade
    total_caixa += valor_compra
    
    print(f"Produto: {produtos[codigo][0]} | Quantidade: {quantidade} | Valor total: R$ {valor_compra:.2f}")
    print("-" * 40)

print(f"Valor total acumulado no caixa: R$ {total_caixa:.2f}")