'''6 – Adicione ao programa da questão anterior, uma opção para excluir o cadastro
baseado no código da pessoa. Adicione também uma opção para pesquisar que utilizará
o nome da pessoa como critério de busca.'''



codigos = [0] * 15
nomes = [0] * 15
idds = [0] * 15
alts = [0] * 15
pesos = [0] * 15


while True:


   print("\nMENU")
   print("1 - Cadastrar")
   print("2 - Excluir")
   print("3 - Alterar")
   print("4 - Listar")
   print("5 - Pesquisar")
   print("0 - Sair")


   op = int(input("Digite a opção: "))


   if op == 1:


       if 0 in codigos:


           posicao = 0


           for codigo in codigos:


               if codigo == 0:


                   codigos[posicao] = int(input("Código: "))
                   nomes[posicao] = input("Nome: ")
                   idds[posicao] = int(input("Idade: "))
                   alts[posicao] = float(input("Altura: "))
                   pesos[posicao] = float(input("Peso: "))


                   print("Cadastro realizado com sucesso!")
                   break


               posicao += 1


       else:
           print("Não há mais espaço para cadastros.")


   elif op == 2:


       codigo = int(input("Digite o código a excluir: "))


       posicao = 0
       encontrado = False


       for cod in codigos:


           if cod == codigo:


               codigos[posicao] = 0
               nomes[posicao] = 0
               idds[posicao] = 0
               alts[posicao] = 0
               pesos[posicao] = 0


               encontrado = True
               print("Cadastro excluído com sucesso!")
               break


           posicao += 1


       if encontrado == False:
           print("Código não encontrado.")


   elif op == 3:


       codigo = int(input("Digite o código da pessoa: "))


       posicao = 0
       encontrado = False


       for cod in codigos:


           if cod == codigo:


               nomes[posicao] = input("Novo nome: ")
               idds[posicao] = int(input("Nova idade: "))
               alts[posicao] = float(input("Nova altura: "))
               pesos[posicao] = float(input("Novo peso: "))


               encontrado = True
               print("Cadastro alterado com sucesso!")
               break


           posicao += 1


       if encontrado == False:
           print("Código não encontrado.")


   elif op == 4:


       print("\nCADASTROS")


       existe = False


       for codigo, nome, idade, altura, peso in zip(codigos, nomes, idds, alts, pesos):


           if codigo != 0:


               existe = True


               print("\nCódigo:", codigo)
               print("Nome:", nome)
               print("Idade:", idade)
               print("Altura:", altura)
               print("Peso:", peso)


       if existe == False:
           print("Nenhum cadastro encontrado.")


   elif op == 5:


       nomepesquisa = input("Digite o nome: ")


       encontrado = False


       for codigo, nome, idade, altura, peso in zip(codigos, nomes, idds, alts, pesos):


           if nome == nomepesquisa:


               encontrado = True


               print("\nCadastro encontrado:")
               print("Código:", codigo)
               print("Nome:", nome)
               print("Idade:", idade)
               print("Altura:", altura)
               print("Peso:", peso)


       if encontrado == False:
           print("Pessoa não encontrada.")


   elif op == 0:


       print("Programa encerrado.")
       break


   else:
       print("Opção inválida.")
