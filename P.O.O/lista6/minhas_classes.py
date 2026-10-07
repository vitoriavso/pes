class Estudante:

    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.idade = 0
        self.cpf = ""

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} {self.sobrenome}, tenho {self.idade} anos e meu CPF é {self.cpf}."
    
class Estudante2:

    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.idade = 0
        self.matricula = ""

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} {self.sobrenome}, tenho {self.idade} anos e minha matrícula é {self.matricula}."

class Professor:
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.disciplina = ""

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} {self.sobrenome}, ensino {self.disciplina}."
    
class Professor2:
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.especializacao = ""
        self.matricula = ""

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} {self.sobrenome}, ensino {self.especializacao}."

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

class Produto:
    def __init__(self, nome, quantidade):
        self.nome= nome
        self.quantidade = quantidade
    
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

class ContaBancaria:
    def __init__(self):
        self.titular = ''
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        return self.saldo
    
class Carro: 
    def __init__(self):
        self.marca = ""
        self.cor = ""

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor