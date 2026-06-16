'''1 - Implemente um programa com um cadastro de idades de 6 alunos utilizando lista. O
programa deve solicitar as idades dos 6 alunos. Após informar todas as idades, deve-se
apresentar apenas as idades que forem maiores ou iguais a 16.'''
idades = [0]*6
idades[0] = int(input("Idade do primeiro aluno: "))
idades[1] = int(input("Idade do segundo aluno: "))
idades[2] = int(input("Idade do terceiro aluno: "))
idades[3] = int(input("Idade do quarto aluno: "))
idades[4] = int(input("Idade do quinto aluno: "))
idades[5] = int(input("Idade do sexto aluno: "))
for elemento in idades:
    if elemento >= 16:
        print('As idades maiores ou iguais a 16 são: ', elemento)