'''3 – Crie uma classe chamada ContaBancaria com:
• Atributos: titular e saldo.
• Um método chamado depositar que recebe um valor e adiciona ao saldo.
• Um método chamado sacar que recebe um valor e subtrai do saldo (não precisa
validar o saldo).
• Um método chamado mostrar_saldo que retorna o saldo atual.
Teste criando uma conta, fazendo depósitos, saques e exibindo o saldo.'''

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
    
# Testando a classe ContaBancaria
conta = ContaBancaria(input("Digite o nome do titular da conta: "))
print(f"Saldo inicial de {conta.titular}: R${conta.mostrar_saldo():.2f}")
conta.depositar(float(input("Digite o valor a ser depositado: ")))
print(f"Saldo atual de {conta.titular}: R${conta.mostrar_saldo():.2f}")
conta.sacar(float(input("Digite o valor a ser sacado: ")))
print(f"Saldo atual de {conta.titular}: R${conta.mostrar_saldo():.2f}")