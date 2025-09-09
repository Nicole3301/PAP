from produto import Produto
from arranjos import Arranjos



class Encomenda():
    lista_encomendas = []
    
    
    def __init__(self, id_encomenda, nome_criador, nome_cliente_encomenda, data_criacao, data_entrega, escolha_produto_desejado, quantidade, preco_total):
        self.Id_encomenda = id_encomenda
        self.Nome_criador = nome_criador
        self.Nome_cliente_encomenda = nome_cliente_encomenda
        self.Data_criacao = data_criacao
        self.Data_entrega = data_entrega
        self.Escolha_produto_desejado = escolha_produto_desejado
        self.Quantidade = quantidade
        self.Preco_total = preco_total
        
    contador_id_encomenda = 1
    def adicionar_encomenda(self):
        id_encomenda = Encomenda.contador_id_encomenda 
        Encomenda.contador_id_encomenda += 1
        
        nome_criador = input("Nome da pessoa que está a criar a encomenda: ").lower()
        
        nome_cliente_encomenda = input("Nome do cliente: ").lower()
        
        while True: 
            try:
                data_criacao = input("Data da criação da encomenda: ")
                break
            except:
                print("A data tem de ser (dia/mês/ano), tente novamente!")
                continue
        
        while True:
            try:
                data_entrega = input("Data de entrega: ")
                break
            except:
                print("A data tem de ser (dia/mês/ano), tente novamente!")
                continue
        
        
        escolha_arranjo_ou_extra = input("Deseja encomendar um arranjo ou comprar um extra? ").lower()
        if escolha_arranjo_ou_extra in ['arranjo', 'Arranjo', 'extra', 'Extra']:
            
        
                
        tipo_de_produto_desejado = input("Arranjo desejado: ").lower()
        if tipo_de_produto_desejado == Arranjos.lista_arranjos:
            for 
        
        
    
        