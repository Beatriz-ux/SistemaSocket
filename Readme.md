# Analisador de Emoções

## Discentes

-   Beatriz Pereira Aragão
-   Isaias Mendes

## Sobre o projeto

Simula um sistema de estoque por intermédio de Sockets TCP, apenas usuários com login e senha conseguem acessar o sistema. Nele é possivel que diferentes usuários consigam acessar informações do estoque em tempo real.

## Protocolo

![Diagrama](./assets/diagrama.png)

1. Usuário se conecta ao Host e Porta, definida previamente nele (host)

2. Informa login e senha

3. É recebido feedback de conexão

    1. Em caso de conexão positiva:

    Retorna o feedback positivo:

    > Usuário logado com sucesso


    2. Caso contrário:

    Retorna apenas uma mensagem de feedback de conexão:

    > Usuário ou senha inválidos

> A partir da conexão feita com sucesso, é mostrado o menu de opções:

```
    1. Cadastrar Produto
    2. Buscar Produto
    3. Listar Produtos
    0. Sair
```

> O usuário pode escolher uma das opções.

4. O usuário envia um comando com a opção e os argumentos.

5. O servidor retorna de acordo com o método que foi solicitado.

6. Os eventos 4 e 5 ficam em LOOP esperando novas interações do usuário, sendo estas interações, um novo comando ou um pedido de saída do sistema.

7. O cliente pode enviar um pedido de saída ao servidor, enviando o comando `0`.

8. O servidor recebe esta mensagem, e desconecta o usuário da aplicação.



## Como instalar

Antes de tudo, você precisa do **Python 3.10** instalado na sua máquina. 

Após isso, você precisa clonar o repositório para a sua máquina. Siga os comandos abaixo:

```bash
git clone https://github.com/beatriz-ux/Socket.git

cd Socket
```

Daqui em diante, recomenda-se a utilização do **Power Shell** no Windows ou do **terminal nativo** no Linux.



## Como executar

Para executar o projeto, você precisa executar o arquivo **server.py** em um terminal e **cliente.py** em outro. Para isso, execute os comandos abaixo:

```bash

python ./server.py

python ./cliente.py

```
