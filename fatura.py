class Fatura():
    def __init__(self, id_venda, total):
        self.Id_venda = id_venda
        self.Lista_produto = []
        self.lista_quantidade = []
        self.total = total
        self.Arranjo = None
        