'''3 – Construa um algoritmo que solicite o nome de usuário e a senha. Se o nome de
usuário for igual a "admin" e a senha for igual a "12345", exiba "Login bem-sucedido".
Caso contrário, exiba "Nome de usuário ou senha incorretos".
'''
nome_usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')
if nome_usuario == 'admin' and senha == '12345':
    print ('Login bem-sucedido')
else:
    print ('Nome de usuário ou senha incorretos')