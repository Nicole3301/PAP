from produto import Produto
from arranjos import Arranjos

class Encomenda():
    lista_encomendas = []
    
    
    
    def __init__(self, id_encomenda, id_cliente, data_criacao, data_entrega):
        self.Id_encomenda = id_encomenda
        self.Id_cliente = id_cliente
        self.Data_criacao = data_criacao
        self.Data_entrega = data_entrega
        self.Lista_produtos = []
        
    contador_id_encomenda = 1
    def adicionar_encomenda(self):
        id_encomenda = Encomenda.contador_id_encomenda 
        Encomenda.contador_id_encomenda += 1
        
        
encomenda = Encomenda("", "", "", "")

      
        
    
        