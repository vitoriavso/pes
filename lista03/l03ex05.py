'''5 – Faça um programa que funcionará como um cadastro de medidas corpóreas. Seu
programa deve ter uma estrutura que seja capaz de armazenar as seguintes informações
sobre cada pessoa: nome, idade, altura e peso (cada uma em uma lista). A interação deve
ser através de um menu com as seguintes opções:
1 – Cadastrar
2 - Excluir
3 - Alterar
4 - Listar
0 - Sair
A opção Cadastrar deve solicitar as informações da pessoa a ser cadastrada. Já a opção
excluir, deve solicitar o nome de quem se deseja excluir o cadastro. A opção Alterar deve
solicitar o nome da pessoa a ser alterado e, em seguida, solicitar as novas informações
da pessoa (idade, altura e peso). A opção Listar deve apresentar todas as informações
das pessoas cadastradas. '''


nomes = [0] * 15
idds = [0] * 15
alts = [0] * 15
pesos = [0] * 15


while True:


   print("\nMENU", "\n1 - Cadastrar", "\n2 - Excluir", "\n3 - Alterar", "\n4 - Listar", "\n0 - Sair")


   op = int(input("Digite a opção: "))


   if op == 1:


       if 0 in nomes:


           posicao = nomes.index(0)


           nome = input("Nome: ")


           if nome in nomes:
               print("Pessoa já cadastrada.")


           else:
               idade = int(input("Idade: "))
               altura = float(input("Altura: "))
               peso = float(input("Peso: "))


               nomes[posicao] = nome
               idds[posicao] = idade
               alts[posicao] = altura
               pesos[posicao] = peso


               print("Cadastro realizado com sucesso!")


       else:
           print("Não há mais espaço.")


   elif op == 2:


       nome = input("Qual pessoa deseja excluir? ")


       if nome in nomes:


           indice = nomes.index(nome)


           nomes[indice] = 0
           idds[indice] = 0
           alts[indice] = 0
           pesos[indice] = 0


           print("Cadastro excluído com sucesso!")


       else:
           print("Pessoa não encontrada.")


   elif op == 3:


       nome = input("Qual pessoa deseja alterar? ")


       if nome in nomes:


           indice = nomes.index(nome)


           idds[indice] = int(input("Nova idade: "))
           alts[indice] = float(input("Nova altura: "))
           pesos[indice] = float(input("Novo peso: "))


           print("Cadastro alterado com sucesso!")


       else:
           print("Pessoa não encontrada.")


   elif op == 4:


       print("\nCADASTROS:")


       for i in range(15):


           if nomes[i] != 0:


               print("\nNome:", nomes[i], "\nIdade:", idds[i], "\nAltura:", alts[i], "m", "\nPeso:", pesos[i], "kg")


   elif op == 0:


       print("Programa encerrado.")
       break


   else:
       print("Opção inválida.")
