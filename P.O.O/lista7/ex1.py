'''1 - Livro e MarcadorDePagina (0..1).
Objetivo: Implementar um relacionamento opcional simples.
Classes: MarcadorDePagina e Livro.
Regras:
• A classe MarcadorDePagina deve ter um atributo pagina_atual.
• A classe Livro deve ter um atributo titulo e um total_paginas.
• Um Livro pode ter zero ou um MarcadorDePagina (ele começa sem marcador,
0..1).
• Crie um método no Livro chamado adicionar_marcador(pagina). Este método deve
criar uma instância de MarcadorDePagina e associá-la ao livro. Se o livro já tiver
um marcador, apenas atualize a pagina_atual dele.'''

from  minhasclasses7 import Livro, MarcadorDePagina

t = input("Digite o título do livro: ")
p = int(input("Digite o total de páginas do livro: "))
livro = Livro(t, p)
livro.adicionar_marcador(200)
livro.adicionar_marcador(300)



