'''2 - Peça a idade de uma pessoa. Usando estruturas de decisão, exiba uma mensagem
com a classificação indicativa permitida para essa pessoa:
• Menor que 10 anos: "Você pode assistir apenas a filmes com classificação Livre."
• Entre 10 e 11 anos: "Você pode assistir a filmes com classificação até 10 anos."
• Entre 12 e 13 anos: "Você pode assistir a filmes com classificação até 12 anos."
• Entre 14 e 15 anos: "Você pode assistir a filmes com classificação até 14 anos."
• Entre 16 e 17 anos: "Você pode assistir a filmes com classificação até 16 anos."
• 18 anos ou mais: "Você pode assistir a filmes com classificação até 18 anos."'''

idade = int(input('Qual é a sua idade?'))
if idade < 10: #menor que 10 anos
    print ('Você pode assistir apenas a filmes com classificação Livre.')
elif idade >= 10 and idade <= 11: #entre 10 e 11
    print ('Você pode assistir a filmes com classificação até 10 anos.')
elif idade >= 12 and idade <= 13: #entre 12 e 13 anos
    print ('Você pode assistir a filmes com classificação até 12 anos.')
elif idade >= 14 and idade <= 15: #entre 14 e 15 anos
    print ('Você pode assistir a filmes com classificação até 14 anos.')
elif idade >= 16 and idade <= 17: #entre 16 e 17 anos
    print ("Você pode assistir a filmes com classificação até 16 anos.")
else: #18 anos ou mais
    print ('Você pode assistir a filmes com classificação até 18 anos.')