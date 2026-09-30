'''5 – Crie uma classe chamada Pessoa com:
• Atributos: nome, idade, altura e peso;
• Um método para exibir, em uma única linha, o nome, a idade, a altura e o peso da
pessoa;
• Um método para retornar o IMC (Índice de Massa Corpórea) calculado da pessoa;
• Um método para retornar apenas o nome e o IMC da pessoa (em uma única linha).
Teste criando 3 pessoas com diferentes atributos e verificando se os IMCs calculados
estão corretos.'''

class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.altura = 0.0
        self.peso = 0.0

    def exibir_dados(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Peso: {self.peso}'

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def exibir_nome_imc(self):
        return f'Nome: {self.nome}, IMC: {self.calcular_imc()}'

pessoa1 = Pessoa()
pessoa1.nome = input("Digite o nome da primeira pessoa: ")
pessoa1.idade = int(input("Digite a idade da primeira pessoa: "))
pessoa1.altura = float(input("Digite a altura da primeira pessoa: "))
pessoa1.peso = float(input("Digite o peso da primeira pessoa: "))

pessoa2 = Pessoa()
pessoa2.nome = input("Digite o nome da segunda pessoa: ")
pessoa2.idade = int(input("Digite a idade da segunda pessoa: "))
pessoa2.altura = float(input("Digite a altura da segunda pessoa: "))
pessoa2.peso = float(input("Digite o peso da segunda pessoa: "))            

pessoa3 = Pessoa()
pessoa3.nome = input("Digite o nome da terceira pessoa: ")
pessoa3.idade = int(input("Digite a idade da terceira pessoa: "))
pessoa3.altura = float(input("Digite a altura da terceira pessoa: "))
pessoa3.peso = float(input("Digite o peso da terceira pessoa: "))

print(pessoa1.exibir_dados())
print(pessoa1.exibir_nome_imc())
print(pessoa2.exibir_dados())
print(pessoa2.exibir_nome_imc())
print(pessoa3.exibir_dados())
print(pessoa3.exibir_nome_imc())