# Exercício 1: Livro e Marcador de Página (0..1).
# Objetivo: Implementar um relacionamento opcional simples.
# Classes: MarcadorDePagina e Livro.
# Regras:
# • A classe MarcadorDePagina deve ter um atributo pagina_atual.
# • A classe Livro deve ter um atributo titulo e um total_paginas.
# • Um Livro pode ter zero ou um MarcadorDePagina (ele começa sem marcador,
# 0..1).
# • Crie um método no Livro chamado adicionar_marcador(pagina). Este método deve
# criar uma instância de MarcadorDePagina e associá-la ao livro. Se o livro já tiver
# um marcador, apenas atualize a pagina_atual dele.
class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual
    def __repr__(self):
        return f"O marcador está na página {self.pagina_atual}"

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None

    def adicionar_marcador(self, pagina):
        if pagina < 1 or pagina > self.total_paginas:
            return "Página inválida."
        else:
            if self.marcador is None:
                self.marcador = MarcadorDePagina(pagina)
            else:
                self.marcador.pagina_atual = pagina
                return f"Marcador atualizado: {self.marcador}"
    def __repr__(self):
        if self.marcador is None:
            return f"\nLivrotitulo = {self.titulo}, total_paginas = {self.total_paginas}, marcador = sem marcador\n"
        else:
            return f"\nLivro: titulo = {self.titulo}, total_paginas = {self.total_paginas}, marcador = {self.marcador}\n"
        
# Exercício 2: Computador e CPU (1..1).
# Objetivo: Implementar um relacionamento obrigatório (Composição).
# Classes: CPU e Computador.
# Regras:
# A classe CPU deve ter atributos fabricante (ex: "Intel") e modelo (ex: "i7-12700K").
# • A classe Computador deve ter um atributo tipo (ex: "Desktop" ou "Notebook").
# • Um Computador deve ter exatamente uma CPU para ser criado (1..1).
# • O __init__ do Computador deve receber os dados necessários para criar sua própria instância de CPU. O atributo computador.cpu nunca pode ser None.
# Comprove o funcionamento da sua implementação no programa principal.
class CPU:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo

    def __repr__(self):
        return f"CPU: fabricante = {self.fabricante}, modelo = {self.modelo}"


class Computador:
    def __init__(self, tipo, fabricante_cpu, modelo_cpu):
        self.tipo = tipo
        self.cpu = CPU(fabricante_cpu, modelo_cpu)

    def __repr__(self):
        return f"Computador: tipo = {self.tipo}, {self.cpu}"

# Exercício 3: VagaDeEstacionamento e Carro (0..1 - Associação Simples)
# Objetivo: Modelar um relacionamento 0..1 onde a "parte" (Carro) vem de fora
# (Agregação/Associação).
# Classes: Carro e VagaDeEstacionamento.
# Regras:
# A classe Carro é simples, tem apenas placa e modelo.
# • A classe VagaDeEstacionamento tem um id_vaga (ex: "A-101").
# • Uma VagaDeEstacionamento pode estar ocupada por zero ou um Carro (0..1). O
# atributo carro_estacionado começa como None.
# • Crie um método ocupar_vaga(carro_obj). Este método deve verificar se a vaga já
# está None. Se estiver livre, associa o carro_obj (vindo de fora) à vaga e retorna
# True. Se já estiver ocupada, não faz nada e retorna False.
# • Crie um método liberar_vaga() que simplesmente seta carro_estacionado de volta
# para None.
# Seu programa principal deve ter um menu interativo onde se possa testar todos os
# métodos de um objeto do tipo VagaDeEstacionamento.

class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo
    def __repr__(self):
        return f"Carro(placa='{self.placa}', modelo='{self.modelo}')"



class VagaDeEstacionamento:
    def __init__(self, id_vaga):
        self.id_vaga = id_vaga
        self.carro_estacionado = None

    def ocupar_vaga(self, carro_obj):
        if self.carro_estacionado is None:
            self.carro_estacionado = carro_obj
            return True
        else:
            return False

    def liberar_vaga(self):
        self.carro_estacionado = None
    
    def __repr__(self):
        return f"VagaDeEstacionamento: id_vaga = '{self.id_vaga}', carro_estacionado = {self.carro_estacionado})"

#Exercício 4: Funcionario e ContratoDeTrabalho (1..1).
#Objetivo: Modelar um 1..1 onde a "parte" (Contrato) é obrigatória e contém a lógica de
#cálculo que o "todo" (Funcionario) utiliza.
#Classes: ContratoDeTrabalho e Funcionario.
#Regras:
#• A classe ContratoDeTrabalho deve ter salario_bruto (float) e percentual_impostos
#(float, ex: 0.11 para 11% de INSS).
#• O ContratoDeTrabalho deve ter um método chamado valor_impostos que calcula e
#retorna o valor exato do desconto (ex: salario_bruto * percentual_impostos).
#• A classe Funcionario deve ter nome e cargo.
#• Um Funcionario deve ter exatamente um ContratoDeTrabalho para ser criado
#(1..1).
#• O __init__ do Funcionario deve receber nome, cargo, e também o salario_bruto e o
#percentual_impostos necessários para criar sua própria instância de
#ContratoDeTrabalho (Composição). O atributo funcionario.contrato nunca pode ser
#None.
#• Crie um método chamado salario_liquido na classe Funcionario. Este método deve:
#◦ Acessar o salario_bruto do seu contrato.
#◦ Acessar o valor_impostos calculado pelo seu contrato.
#◦ Retornar o salario_bruto menos o valor_impostos.
#Seu programa principal deve ter um menu interativo onde se possa testar todos os
#métodos de um objeto do tipo Funcionario. Faça, também, o Diagrama de Classes da sua
#implementação final.

class ContratoDeTrabalho:
    def __init__(self, salario_bruto, percentual_impostos):
        self.salario_bruto = salario_bruto
        self.percentual_impostos = percentual_impostos

    def valor_impostos(self):
        return self.salario_bruto * self.percentual_impostos
    
    def __repr__(self):


class Funcionario:
    def __init__(self, nome, cargo, salario_bruto, percentual_impostos):
        self.nome = nome
        self.cargo = cargo

        self.contrato = ContratoDeTrabalho(
            salario_bruto, percentual_impostos
        )

    def salario_liquido(self):
        impostos = self.contrato.valor_impostos()


        return self.contrato.salario_bruto - impostos