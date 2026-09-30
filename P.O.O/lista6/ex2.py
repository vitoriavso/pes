'''2 – Crie uma classe chamada Carro com:
• Atributos: marca e cor.
• Um método chamado pintar que recebe uma nova cor como argumento e altera o
atributo cor para essa nova cor.
• Um método chamado mostrar_cor que retorna a cor atual do carro.
Teste criando um objeto, alterando sua cor com o método pintar e exibindo a nova cor
com mostrar_cor.'''

class Carro: 
    def __init__(self):
        self.marca = ""
        self.cor = ""

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor

carro1 = Carro()
carro1.marca = input("Digite a marca do carro: ")
carro1.cor = input("Digite a cor do carro: ")
carro1.pintar(input("Digite a nova cor do carro: "))
print(carro1.mostrar_cor())