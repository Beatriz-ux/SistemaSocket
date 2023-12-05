class Produto:
    id_gerado = 0

    def __init__(self, nome, preco):
        Produto.id_gerado += 1
        self.id = Produto.id_gerado
        self.nome = nome
        self.preco = preco

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco
    
    def get_id(self):
        return self.id

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco


    def __str__(self):
        return f"Id: {self.id} - Nome: {self.nome} - Preço: {self.preco}"
    
    