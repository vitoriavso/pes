class Estudante:

    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.idade = 0
        self.cpf = ""

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} {self.sobrenome}, tenho {self.idade} anos e meu CPF é {self.cpf}."

class Professor:
    def __init__(self):
        self.nome = ""
        self.sobrenome = ""
        self.disciplina = ""

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} {self.sobrenome}, ensino {self.disciplina}."
