from socket import * 
import threading
from Users import *


from funcoes import *
from Produto import *
HOST = gethostname() #pega o nome da maquina local
PORT = 12000 #porta que o servidor vai escutar

server=socket(AF_INET,SOCK_STREAM) #criando o socket
server.bind((HOST,PORT)) #host e porta ,host é o endereco do servidor e a porta é a porta do servidor
server.listen(2) #numero de clientes que podem se conectar ao mesmo tempo

print("Servidor de nome",HOST,"esperando conexão na porta",PORT)

#loop infinito para permitir que o servidor fique sempre escutando conexoes
while True:
    #aceita a conexao
    connection, address = server.accept() # verifica novas conexoes
    print("Conexão estabelecida com ", address)

    #recebe a mensagem do cliente
    message = connection.recv(1024)
    #decodifica a mensagem, pois ela vem em bytes
    message = message.decode()
    username = message.split(";")[0]
    password = message.split(";")[1]

    if(login(username, password)):
        connection.send("Usuário logado com sucesso".encode())
    else:
        connection.send("invalid_credentials".encode())

    #cria uma thread para tratar a conexao
    thread = threading.Thread(target=novaMensagem, args=(connection, address))
    thread.start()




