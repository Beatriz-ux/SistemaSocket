from socket import *
from funcoes import *

#criando o socket
client = socket(AF_INET, SOCK_STREAM)

def main():
    HOST = input("Digite o host do servidor: ")
    PORT = int(input("Digite a porta do servidor: "))
    #conectando ao servidor
    try:
        client.connect((HOST, PORT))
    except Exception as e:
        print("Erro ao conectar ao servidor: ", e)
        return
    
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    msg = f"{username};{password}"
    client.send(msg.encode())

    while True:
        msg = client.recv(1024)
        msg = msg.decode()
        
        if(msg == "invalid_credentials"):
            print("Usuário ou senha inválidos!")
            client.close()
            return
        elif(msg == "close"):
            print("Desconectando!")
            client.close()
            return
        
        print("--------------")
        print(msg)
        print("--------------\n")
        opcao = menuInicial()
        if opcao == '1':
            p,qtd = cadastrarProduto()
            msg = f"{opcao};{p.get_nome()};{p.get_preco()};{qtd}"
            client.send(msg.encode())
        elif opcao == '2':
            id=buscarProduto()
            msg = f"{opcao};{id}"
            client.send(msg.encode())
        elif opcao == '3':
            msg = f"{opcao}"
            client.send(msg.encode())
        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            client.send("-1".encode())
    


if __name__ == '__main__':
    main()
