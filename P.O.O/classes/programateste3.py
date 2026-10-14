class CarteiraDeMotorista:
    def __init__(self, numero, categoria):
        self.numero = numero
        self.categoria = categoria
    def __repr__(self):
        return f"CarteiraDeMotorista(numero={self.numero}, categoria={self.categoria})"

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.cnh = None
    def tirar_habilitacao(self, numero, categoria):
        if self.cnh is None:
            self.cnh = CarteiraDeMotorista(numero, categoria)
        else:
            print(f"{self.nome} já possui uma CNH: {self.cnh}")
    def eh_habilitada(self):
        if self.cnh is None:
            return "A pessoa não possui habilitação."
        else:
            return 'A pessoa possui habilitação.'
        
    def __repr__(self):
        return f"Pessoa: nome={self.nome}, cnh={self.cnh}"
    
# Programa Principal - primeira parte
print("Criando o objeto...")
n = input("Digite o nome da pessoa: ")
pesssoinha = Pessoa(n)

print(f"Objeto criado: {pesssoinha}")

# --- Verificando o estado inicial ('0') ---
print(f"A {pesssoinha.nome} é habilitada? {pesssoinha.eh_habilitada()}")

# --- Mudando o estado para '1' ---
print(f"\n{pesssoinha.nome} foi tirar a habilitação...")
num = input(f"Digite o número da CNH para {pesssoinha.nome}: ")
cat = input(f"Digite a categoria da CNH para {pesssoinha.nome}: ").upper()

pesssoinha.tirar_habilitacao(num, cat)

print(f"CNH da {pesssoinha.nome}: {pesssoinha.cnh}")  # O atributo é None


sucesso = pesssoinha.tirar_habilitacao(num, cat)
if sucesso is not None:
    print(sucesso) 
else:
    print(f"{pesssoinha.nome} não conseguiu tirar a habilitação.")

print(f"A {pesssoinha.nome} é habilitada? {pesssoinha.eh_habilitada()}")
print(f"CNH da {pesssoinha.nome}: {pesssoinha.cnh}")  # O atributo agora é um objeto CarteiraDeMotorista
print(f"Número da CNH: {pesssoinha.cnh.numero}, Categoria: {pesssoinha.cnh.categoria}")