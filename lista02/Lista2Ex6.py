'''6 - Modifique o programa anterior de forma que o usuário também digite o início e o fim da
tabuada, em vez de começar iniciar no 1 e terminar no 10.'''

inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
n = int(input("Informe um número: "))

x = inicio

while x <= fim:
    print(n, "x", x, "=", n * x)
    x = x + 1