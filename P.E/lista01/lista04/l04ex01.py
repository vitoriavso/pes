'''1 – Implemente um algoritmo com uma lista de nomes de bairros de Garopaba. O nome
do primeiro bairro deve ser adicionado manualmente (no próprio programa), em seguida,
deve ser solicitado ao usuário para cadastrar o nome de mais 5 bairros. Ao final, o
programa deve exibir o nome de todos os bairros cadastrados na tela.'''

indice = 0
nomes = ['Grama']

while indice < 5:
    nome = (input("Digite o nome de um bairro de Garopaba:"))
    if nome in nomes:
        print('Bairro já cadastrado.')
    else:
        nomes.append(nome)
    indice = indice + 1

for elemento in nomes:
    print("É um bairro de Garopaba: ", elemento)