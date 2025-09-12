from datetime import date 
from datetime import datetime 

class Promocao():
    def __init__(self, id_promocao, data_inicio, data_fim):
        self.Id_promocao = id_promocao
        self.Data_inicio = data_inicio
        self.Data_fim = data_fim
        #self.incremento = bool
        #self.percentagem = 15
    
    contador_id_promocao = 1    
    def adicionar_promocoes(self):
        id_promocao = Promocao.contador_id_promocao
        Promocao.contador_id_promocao += 1
        
        data_inicio = date.today()
        print(data_inicio)
        
        data_fim_str = input("Insira a hora que vai agendada a encomenda: ")
        data_fim = datetime.strftime(data_fim_str, '%d/%m/%Y')
        print(data_fim)
        
        
promocao = Promocao("", "", "")  
promocao.adicionar_promocoes()    