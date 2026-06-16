'''7 – Implemente um programa para calcular sua média final em uma determinada unidade
curricular. O programa deve solicitar ao usuário a quantidade de notas, o valor para cada
uma das notas e exibir, ao final, a média aritmética simples e informar se o(a) estudante
está Aprovado ou Reprovado. Considere que a média mínima para a aprovação é 6.'''

qtd_notas = int(input('Quantas notas haverá? '))
nota = 0
valor_nota = 0
valor_tot = 0
while nota < qtd_notas:
    valor_nota = float(input('Qual é o valor da nota? '))
    valor_tot= valor_tot + valor_nota
    nota = nota + 1 
media = valor_tot / qtd_notas

if media < 6:
    print ('Reprovado')
else: 
    print('Aprovado')