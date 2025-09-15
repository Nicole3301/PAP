from datetime import date 
from datetime import datetime 

class Promocao():

    
    def __init__(self, id_promocao, data_inicio, data_fim):
        self.Id_promocao = id_promocao
        self.Data_inicio = data_inicio
        self.Data_fim = data_fim
        #self.incremento = bool
        #self.desconto = 15
    
    contador_id_promocao = 1    
    def adicionar_promocoes(self):
        id_promocao = Promocao.contador_id_promocao
        Promocao.contador_id_promocao += 1
        
        data_inicio = date.today()
        print(data_inicio)
        
        
        data_fim_str = input("Data da promoção (dd-mm-yyyy): ")
        data_fim = data_fim_str.strptime("%d-%m-%Y")
        print(data_fim) 
        
promocao = Promocao("", "", "")  
promocao.adicionar_promocoes()    