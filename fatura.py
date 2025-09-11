class Fatura():
    
    def __init__(self, id_venda, total):
        self.Id_venda = id_venda
        self.total = total
        self.Arranjo = None
        
    contador_id_venda = 1
    def adicionar_fatura(self):
        id_venda = Fatura.contador_id_venda
        Fatura.contador_id_venda += 1 
        
        