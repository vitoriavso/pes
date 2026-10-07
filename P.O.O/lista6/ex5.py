'''5 – Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.'''

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir_dados(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Peso: {self.peso}'

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def exibir_nome_imc(self):
        return f'Nome: {self.nome}, IMC: {self.calcular_imc()}'

n = input("Digite o nome da primeira pessoa: ")
i = int(input("Digite a idade da primeira pessoa: "))
a = float(input("Digite a altura da primeira pessoa: "))
p = float(input("Digite o peso da primeira pessoa: "))
pessoa1 = Pessoa(n, i, a, p)

n2 = input("Digite o nome da segunda pessoa: ")
i2 = int(input("Digite a idade da segunda pessoa: "))
a2 = float(input("Digite a altura da segunda pessoa: "))
p2 = float(input("Digite o peso da segunda pessoa: "))
pessoa2 = Pessoa(n2, i2, a2, p2)

n3 = input("Digite o nome da terceira pessoa: ")
i3 = int(input("Digite a idade da terceira pessoa: "))
a3 = float(input("Digite a altura da terceira pessoa: "))
p3 = float(input("Digite o peso da terceira pessoa: "))
pessoa3 = Pessoa(n3, i3, a3, p3)

print(pessoa1.exibir_dados())
print(pessoa1.exibir_nome_imc())
print(pessoa2.exibir_dados())
print(pessoa2.exibir_nome_imc())
print(pessoa3.exibir_dados())
print(pessoa3.exibir_nome_imc())