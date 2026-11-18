

# CLASSE NOTEBOOK

class Notebook:
    def __init__(self, patrimonio, marca):
        self.patrimonio = patrimonio
        self.marca = marca

    def __repr__(self):
        return f"Notebook -> patrimonio: {self.patrimonio} | marca: {self.marca}"


# CLASSE BANCADA

class Bancada:
    def __init__(self, numero):
        self.numero = numero
        self.notebook_atual = None

    def colocar(self, notebook):
        if self.notebook_atual is None:
            self.notebook_atual = notebook
            return True
        else:
            return False

    def retirar(self):
        self.notebook_atual = None

    def __repr__(self):
        return f"Bancada -> numero: {self.numero} | notebook_atual: {self.notebook_atual}"