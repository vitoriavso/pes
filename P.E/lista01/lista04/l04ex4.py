'''4 – Faça um algoritmo que solicite ao usuário a quantidade de cidades que devem ser
cadastradas em uma lista. Em seguida, faça a leitura das cidades e imprima o resultado
na tela. Ao final, solicite ao usuário o nome de uma cidade para ser removida, faça a
remoção dela e imprima a lista novamente.'''

qtd = int(input('Quantas cidades devem ser cadastradas? '))
indice = 0
cidades = []

while indice < qtd:
    cidade = input("Digite a cidade: ")
    if cidade in cidades:
       print('Cidade já cadastrada.')
    else:
        cidades.append(cidade)
        indice = indice + 1

quantidade = len(cidades)
indice = 0

while indice < quantidade:
 print("cidade: ", cidades[indice])
 indice = indice + 1

print('Remova uma cidade.')
exclui =input('Qual cidade você removerá? ')

if exclui in cidades:
    print("Excluindo...")
    cidades.remove(exclui)
else:
    print('Não foi possível excluir esta cidade, pois ela não existe no nosso sistema!')

quantidade = len(cidades)
indice = 0

while indice < quantidade:
 print("cidade: ", cidades[indice])
 indice = indice + 1