
import hashlib
import pickle
import os
from datetime import datetime

# CLASSE USUARIO

class Usuario:
    def __init__(self, nome, login, senha, tipo):
        self.nome = nome
        self.login = login
        self.senha = self.gerar_hash(senha)
        self.tipo = tipo

    def gerar_hash(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha):
        return self.senha == self.gerar_hash(senha)

    def __repr__(self):
        return (
            f"{self.nome} | Login: {self.login} | "
            f"Tipo: {self.tipo}"
        )


# CLASSE PRODUTO

class Produto:
    def __init__(self, id_produto, nome, categoria, tamanho, preco, estoque):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.tamanho = tamanho
        self.preco = preco
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.estoque += quantidade
            return True
        return False

    def retirar_estoque(self, quantidade):
        if 0 < quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        return False

    def __repr__(self):
        return (
            f"ID: {self.id_produto} | {self.nome} | "
            f"{self.categoria} | Tamanho: {self.tamanho} | "
            f"R$ {self.preco:.2f} | Estoque: {self.estoque}"
        )


# CLASSE ITEM DE VENDA


class ItemVenda:
    def __init__(self, produto, quantidade):
        self.nome = produto.nome
        self.quantidade = quantidade
        self.preco = produto.preco

    def calcular_subtotal(self):
        return self.quantidade * self.preco

    def __repr__(self):
        return (
            f"{self.nome} | Quantidade: {self.quantidade} | "
            f"Subtotal: R$ {self.calcular_subtotal():.2f}"
        )


# CLASSE VENDA

class Venda:
    def __init__(self, id_venda, cliente, itens):
        self.id_venda = id_venda
        self.cliente = cliente
        self.data = datetime.now()
        self.itens = itens
        self.total = sum(
            item.calcular_subtotal() for item in itens
        )

    def __repr__(self):
        return (
            f"Venda {self.id_venda} | Cliente: {self.cliente} | "
            f"Data: {self.data.strftime('%d/%m/%Y %H:%M')} | "
            f"Total: R$ {self.total:.2f}"
        )


# CLASSE LOJA


class Loja:
    def __init__(self):
        self.usuarios = []
        self.produtos = []
        self.vendas = []

        self.proximo_id_produto = 1
        self.proximo_id_venda = 1

        self.carregar_dados()

   
    # SALVAR DADOS COM PICKLE

    def salvar_dados(self):
        dados = {
            "usuarios": self.usuarios,
            "produtos": self.produtos,
            "vendas": self.vendas,
            "proximo_id_produto": self.proximo_id_produto,
            "proximo_id_venda": self.proximo_id_venda
        }

        with open("anvi_gym.pkl", "wb") as arquivo:
            pickle.dump(dados, arquivo)

        print("Dados salvos com sucesso!")

    
    # CARREGAR DADOS COM PICKLE

    def carregar_dados(self):
        if os.path.exists("anvi_gym.pkl"):

            try:
                with open("anvi_gym.pkl", "rb") as arquivo:
                    dados = pickle.load(arquivo)

                self.usuarios = dados["usuarios"]
                self.produtos = dados["produtos"]
                self.vendas = dados["vendas"]

                self.proximo_id_produto = dados["proximo_id_produto"]
                self.proximo_id_venda = dados["proximo_id_venda"]

                print("Dados carregados com sucesso!")

            except (EOFError, pickle.UnpicklingError, KeyError, TypeError):
                print("Erro ao carregar os dados!")
                print("O arquivo pode estar corrompido.")

        else:
            print("Nenhum arquivo de dados encontrado.")
            print("Iniciando um novo sistema Anvi Gym.")

    
    # CADASTRO DE USUARIOS
    

    def buscar_usuario(self, login):
        for usuario in self.usuarios:
            if usuario.login == login:
                return usuario

        return None

    def cadastrar_usuario(self, tipo):
        print("\n--- CADASTRO DE CONTA ---")

        nome = input("Nome completo: ").strip()
        login = input("Nome de usuário: ").strip()

        if not nome or not login:
            print("Nome e login são obrigatórios!")
            return

        if self.buscar_usuario(login):
            print("Este nome de usuário já está cadastrado!")
            return

        senha = input("Senha (mínimo 6 caracteres): ")
        confirmar = input("Confirme a senha: ")

        if len(senha) < 6:
            print("A senha precisa ter pelo menos 6 caracteres!")
            return

        if senha != confirmar:
            print("As senhas não correspondem!")
            return

        usuario = Usuario(nome, login, senha, tipo)

        self.usuarios.append(usuario)

        self.salvar_dados()

        print(f"\nConta {tipo} criada com sucesso!")

    
    # PRIMEIRO ADMINISTRADOR
    

    def configurar_primeiro_admin(self):
        administradores = [
            usuario for usuario in self.usuarios
            if usuario.tipo == "admin"
        ]

        if administradores:
            print("Já existe um administrador cadastrado!")
            return

        print("\n--- PRIMEIRO ADMINISTRADOR ---")

        self.cadastrar_usuario("admin")

    
    # LOGIN
    

    def login(self):
        print("\n--- LOGIN ANVI GYM ---")

        login = input("Usuário: ").strip()
        senha = input("Senha: ")

        usuario = self.buscar_usuario(login)

        if usuario is None:
            print("Usuário não encontrado!")
            return None

        if not usuario.validar_senha(senha):
            print("Senha incorreta!")
            return None

        print(f"\nBem-vindo(a), {usuario.nome}!")

        return usuario

    
    # CADASTRAR PRODUTOS
    

    def cadastrar_produto(self):
        print("\n--- CADASTRO DE PRODUTO ---")

        nome = input("Nome do produto: ").strip()
        categoria = input("Categoria: ").strip()
        tamanho = input("Tamanho: ").strip()

        if not nome or not categoria or not tamanho:
            print("Preencha todos os campos!")
            return

        try:
            preco = float(input("Preço: R$ "))
            estoque = int(input("Quantidade em estoque: "))

            if preco <= 0 or estoque < 0:
                print("Preço inválido ou estoque negativo!")
                return

        except ValueError:
            print("Digite valores numéricos válidos!")
            return

        produto = Produto(
            self.proximo_id_produto,
            nome,
            categoria,
            tamanho,
            preco,
            estoque
        )

        self.produtos.append(produto)
        self.proximo_id_produto += 1

        self.salvar_dados()

        print("Produto cadastrado com sucesso!")

    def listar_produtos(self):
        print("\n--- CATÁLOGO DE PRODUTOS ---")

        if not self.produtos:
            print("Nenhum produto cadastrado.")
            return

        for produto in self.produtos:
            print(produto)

    # BUSCAR PRODUTO
    

    def buscar_produto(self, id_produto):
        for produto in self.produtos:
            if produto.id_produto == id_produto:
                return produto

        return None

    
    # ATUALIZAR ESTOQUE
   

    def atualizar_estoque(self):
        print("\n--- ATUALIZAÇÃO DE ESTOQUE ---")

        self.listar_produtos()

        try:
            id_produto = int(input("\nID do produto: "))
            quantidade = int(input("Quantidade a adicionar: "))

        except ValueError:
            print("Digite números válidos!")
            return

        produto = self.buscar_produto(id_produto)

        if produto is None:
            print("Produto não encontrado!")
            return

        if produto.adicionar_estoque(quantidade):

            self.salvar_dados()

            print("Estoque atualizado com sucesso!")
            print(f"Estoque atual: {produto.estoque}")

        else:
            print("A quantidade precisa ser maior que zero!")

    
    # GERENCIAR CONTAS
  

    def listar_usuarios(self):
        print("\n--- CONTAS CADASTRADAS ---")

        if not self.usuarios:
            print("Nenhuma conta cadastrada.")
            return

        for usuario in self.usuarios:
            print(usuario)


    # COMPRAR PRODUTOS

    def comprar_produto(self, usuario):
        print("\n--- COMPRAR PRODUTOS ---")

        if not self.produtos:
            print("Não existem produtos disponíveis.")
            return

        itens_venda = []
        quantidades = {}

        while True:

            self.listar_produtos()

            try:
                id_produto = int(input("\nID do produto: "))
                quantidade = int(input("Quantidade desejada: "))

            except ValueError:
                print("Digite números válidos!")
                continue

            produto = self.buscar_produto(id_produto)

            if produto is None:
                print("Produto não encontrado!")
                continue

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero!")
                continue

            quantidade_total = (
                quantidades.get(id_produto, 0) + quantidade
            )

            if quantidade_total > produto.estoque:
                print("Estoque insuficiente!")
                continue

            quantidades[id_produto] = quantidade_total

            print("Produto adicionado ao carrinho!")

            continuar = input(
                "Deseja adicionar outro produto? (s/n): "
            ).lower()

            if continuar != "s":
                break

        if not quantidades:
            print("Compra cancelada.")
            return

        for id_produto, quantidade in quantidades.items():

            produto = self.buscar_produto(id_produto)

            item = ItemVenda(produto, quantidade)

            itens_venda.append(item)

        venda = Venda(
            self.proximo_id_venda,
            usuario.login,
            itens_venda
        )

        print("\n--- RESUMO DA COMPRA ---")

        for item in venda.itens:
            print(item)

        print(f"\nTOTAL: R$ {venda.total:.2f}")

        confirmar = input("Confirmar compra? (s/n): ").lower()

        if confirmar != "s":
            print("Compra cancelada.")
            return

        for id_produto, quantidade in quantidades.items():

            produto = self.buscar_produto(id_produto)

            produto.retirar_estoque(quantidade)

        self.vendas.append(venda)
        self.proximo_id_venda += 1

        self.salvar_dados()

        print("\nCompra realizada com sucesso!")

 
    # MINHAS COMPRAS

    def minhas_compras(self, usuario):
        print("\n--- MINHAS COMPRAS ---")

        compras = [
            venda for venda in self.vendas
            if venda.cliente == usuario.login
        ]

        if not compras:
            print("Você ainda não realizou nenhuma compra.")
            return

        for venda in compras:

            print(f"\n{venda}")

            for item in venda.itens:
                print(item)

    # RELATORIOS DE VENDAS

    def relatorios_vendas(self):
        print("\n--- RELATÓRIOS DE VENDAS ---")

        if not self.vendas:
            print("Nenhuma venda registrada.")
            return

        total = sum(
            venda.total for venda in self.vendas
        )

        quantidade_produtos = sum(
            item.quantidade
            for venda in self.vendas
            for item in venda.itens
        )

        print(f"Total de vendas: {len(self.vendas)}")
        print(f"Produtos vendidos: {quantidade_produtos}")
        print(f"Faturamento: R$ {total:.2f}")

        print("\n--- HISTÓRICO DE VENDAS ---")

        for venda in self.vendas:

            print(f"\n{venda}")

            for item in venda.itens:
                print(item)


# MENU DE GERENCIAMENTO DE CONTAS


def menu_contas(loja):

    while True:

        print("\n================================")
        print("       GERENCIAR CONTAS")
        print("================================")
        print("1 - Cadastrar administrador")
        print("2 - Cadastrar usuário")
        print("3 - Listar todas as contas")
        print("0 - Voltar")
        print("================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            loja.cadastrar_usuario("admin")

        elif opcao == "2":

            loja.cadastrar_usuario("user")

        elif opcao == "3":

            loja.listar_usuarios()

        elif opcao == "0":

            break

        else:

            print("Opção inválida!")

