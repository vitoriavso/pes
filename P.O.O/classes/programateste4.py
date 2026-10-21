class Motor:
    def __init__(self, potencia: int):
        self.potencia = potencia
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False
    
    def esta_ligado(self):
        return self.ligado

    def __repr__(self):
        return f"Motor: potencia = {self.potencia} cavalos, ligado = {self.ligado}"




class Carro:
    def __init__(self, modelo: str, ano: int, motor_potencia: int):
        self.modelo = modelo
        self.ano = ano
        self.motordocarro = Motor(motor_potencia)

    def __repr__(self):
        return f"Carro: modelo = {self.modelo}, ano = {self.ano}; {self.motordocarro}"
    
    def ligar_motor(self):
        self.motordocarro.ligar()
    def desligar_motor(self):
        self.motordocarro.desligar()
    def esta_motor_ligado(self):
        return self.motordocarro.esta_ligado()
    

#programa principal
print("Criando o carro...")
m = input("Digite o modelo do carro: ")
a = int(input("Digite o ano do carro: "))
pm = int(input("Digite a potência do motor (em cavalos): "))
car = Carro(m, a, pm)
# primeiro teste
print(f"Carro criado: {car}")
# segundo teste
car.ligar_motor()
print(f"Motor ligado: {car.esta_motor_ligado()}")
# terceiro teste
car.desligar_motor()
print(f"Motor desligado: {car.esta_motor_ligado()}")