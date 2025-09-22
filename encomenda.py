from produto import Produto
from cliente import Cliente
from datetime import date 

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
        
        lista_clientes_encontrados = []
        nome_cliente = input("Nome do cliente: ").lower()
        
        for cliente in Cliente.lista_clientes:
                if nome_cliente in cliente.Nome_cliente.lower():
                    lista_clientes_encontrados.append(cliente)
        
        if len(lista_clientes_encontrados) > 1:
            for i, cliente in enumerate(lista_clientes_encontrados, start=1):
                print(f"{i}- Id: {cliente.Id_cliente} | Nome: {cliente.Nome_cliente} | Contacto: {cliente.Contacto_cliente} | Email: {cliente.Email} |Morada: {cliente.Morada} | Gênero: {cliente.Genero}")
            escolha = int(input("Qual é que deseja editar? "))
            cliente = lista_clientes_encontrados[escolha-1]
        else:
            cliente = lista_clientes_encontrados[0]
            
        data_criacao = input("")
            
            
            

        
encomenda = Encomenda("", "", "", "")
encomenda.adicionar_encomenda()

      
        
    
        