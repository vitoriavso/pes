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

from  minhasclasses7 import Livro

print("--- Criando o livro ---")

t = input("Digite o título do livro: ")
p = int(input("Digite o total de páginas do livro: "))
livro = Livro(t, p)
print(livro)

r1 = input("Deseja adicionar um marcador? (s/n): ").lower()
if r1 == 's':
    print (livro.adicionar_marcador(int(input("Digite a página do marcador: "))))
else:
    print("Nenhum marcador adicionado.")

r2 = input("Deseja atualizar o marcador? (s/n): ").lower()
if r2 == 's':
    print( livro.adicionar_marcador(int(input("Digite a nova página do marcador: "))) )
else:
    print("Marcador não atualizado.")

print(f"Livro: {livro.titulo}")
print(f"Total de páginas: {livro.total_paginas}")
if livro.marcador:
    print(livro.marcador)
else:
    print("Sem marcador de página.")

