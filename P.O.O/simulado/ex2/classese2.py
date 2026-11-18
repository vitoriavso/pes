
# CLASSE REGISTRO DE ABERTURA

class RegistroDeAbertura:
    def __init__(self, data_hora, descricao):
        self.data_hora = data_hora
        self.descricao = descricao

    def resumo(self):
        return f"Data e hora: {self.data_hora}\nDescrição: {self.descricao}"

    def __repr__(self):
        return f"RegistroDeAbertura -> data_hora: {self.data_hora} | descricao: {self.descricao}"


# CLASSE ANOTACAO

class Anotacao:
    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor

    def __repr__(self):
        return f"Anotacao -> texto: {self.texto} | autor: {self.autor}"


# CLASSE CHAMADO

class Chamado:
    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.registro = RegistroDeAbertura(data_hora, descricao)
        self.anotacoes = []

    def adicionar_anotacao(self, texto, autor):
        anotacao = Anotacao(texto, autor)
        self.anotacoes.append(anotacao)

    def relato(self):
        resultado = f"CHAMADO: {self.titulo}\n"
        resultado += "\n--- REGISTRO DE ABERTURA ---\n"
        resultado += self.registro.resumo()

        resultado += "\n\n--- ANOTAÇÕES ---\n"

        if len(self.anotacoes) == 0:
            resultado += "Nenhuma anotação registrada."
        else:
            for anotacao in self.anotacoes:
                resultado += f"\nAutor: {anotacao.autor}"
                resultado += f"\nTexto: {anotacao.texto}\n"

        return resultado

    def __repr__(self):
        return f"Chamado -> titulo: {self.titulo} | registro: {self.registro} | anotacoes: {self.anotacoes}"

