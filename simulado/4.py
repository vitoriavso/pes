'''4 – Crie um dicionário de palavras da língua portuguesa, utilizando as palavras como chaves e seus
significados como valores. Inicie com:
"apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma
situação difícil, ou usar de meios extremos e exagerados"
Solicite ao usuário mais 4 palavras e seus respectivos significados. Em seguida, peça uma
palavra para consulta e exiba seu significado. Caso ela não esteja cadastrada, informe “Palavra
não encontrada”.'''

dic = {'Apelar' : 'recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados'
       }

for i in range(4):
    palavra = input("Digite a palavra: ")
    sign = input('digite seu significado: ')
    dic[palavra] = sign

while True:
    resposta = input('Qual palavra você deseja verifcar o significado? ')
    if resposta not in dic:
        print('Essa palavra não existe no nosso dicionário.')
        print('Tente outra palavra.')
        continue
    if resposta in dic:
        print(f'O significado da palavra {resposta} é: ', dic[resposta])
    rspt = input('Você deseja verificar outra palavra (s/n)? ')
    if rspt == 's':
        continue
    else:
        print('\nSaindo do programa ...\n')
        break

