from Produto import Produto
from Estoque import *
estoque = Estoque()

def menuInicial():
    print("\n")
    print("1. Cadastrar Produto")
    print("2. Buscar Produto")
    print("3. Listar Produtos")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def cadastrarProduto():
    print("- Cadastrar Produto -")
    nome= input("Digite o nome: ")
    preco = float(input("Digite o preço: "))
    qtd = int(input("Digite a quantidade: "))
    p1 = Produto(nome, preco)
    return p1, qtd

def buscarProduto():
    print("- Buscar Produto -")
    id = int(input("Digite o id do produto: "))
    return id


def novaMensagem(connection, endereco):
    while True:
        message = connection.recv(1024)
        #decodifica a mensagem, pois ela vem em bytes
        message = message.decode()
        opcao = message.split(";")[0]
        if opcao == '1':
            nome = message.split(";")[1]
            preco = message.split(";")[2]
            qtd = message.split(";")[3]
            p = Produto(nome, preco)
            estoque.adicionar_produto(p, qtd)
            texto = f"Produto {nome} adicionado com ID {p.get_id()}"
            print(texto)
            connection.send(texto.encode())
        elif opcao == '2':
            id = message.split(";")[1]
            produto = estoque.buscar_produto(id)
            texto = ""
            if produto == None:
                texto = f"Produto não encontrado"
            else:
                texto = f"Produto encontrado: {produto[0]}"
            connection.send(texto.encode())
        elif opcao == '3':
            print("Listar Produtos")
            connection.send(estoque.listar_produtos().encode())
        elif opcao == '0':
            print("Saindo do sistema...")
            connection.close()
            break
        else:
            print("Opção inválida!")
            connection.send("-1".encode())