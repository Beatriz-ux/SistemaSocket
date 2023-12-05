class Estoque:
    def __init__(self):
        self.produtos = []
    
    def get_produtos(self):
        return self.produtos
    
    def set_produtos(self, produtos):
        self.produtos = produtos

    def adicionar_produto(self, produto, quantidade):
        self.produtos.append((produto, quantidade))

    def buscar_produto(self, id):
        for produto in self.produtos:
            if produto[0].get_id() == int(id):
                return produto
        return None

    def listar_produtos(self):
        texto = ""
        for produto in self.produtos:
            texto += (f"{produto[0]} - Quantidade: {produto[1]}\n")
        
        return texto

   