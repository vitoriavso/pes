'''4 – Crie uma classe chamada Produto com:
• Atributos: nome e quantidade.
• Um método chamado esta_disponivel que retorna True se a quantidade for maior
que 0 e False caso contrário.
• Um método chamado vender que diminui a quantidade em 1.
Teste criando um objeto, verificando a disponibilidade, vendendo produtos e verificando
novamente.'''

class Produto:
    def __init__(self):
        self.nome= ''
        self.quantidade = 0
    
    def esta_disponivel(self):
        return self.quantidade > 0
    def resposta_disponibilidade(self):
        if self.esta_disponivel():
            return f'Produto {self.nome} está disponível para venda.'
        else:
            return f'Produto {self.nome} não está disponível para venda.'
    def vender(self):
        if self.esta_disponivel():
            self.quantidade -= 1
            return f'Produto {self.nome} vendido. Quantidade restante: {self.quantidade}'
        else:
            return f'Produto {self.nome} não disponível para venda.'

produto1 = Produto()
produto1.nome = input("Digite o nome do produto: ")
produto1.quantidade = int(input("Digite a quantidade do produto: "))
print(produto1.resposta_disponibilidade())
resposta = input("Deseja vender o produto? (s/n): ")
if resposta.lower() == 's':
    print(produto1.vender())
    print(produto1.resposta_disponibilidade())
else:
    print("Venda cancelada.")