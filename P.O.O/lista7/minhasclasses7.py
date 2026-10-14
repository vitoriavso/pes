class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual
    def __repr__(self):
        return f"MarcadorDePagina(pagina_atual={self.pagina_atual})"

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None

    def adicionar_marcador(self, pagina):
        if self.marcador is None:
            self.marcador = MarcadorDePagina(pagina)
        else:
            self.marcador.pagina_atual = pagina
            print(f"Marcador atualizado: {self.marcador}")

