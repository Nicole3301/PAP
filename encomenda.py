from cliente import Cliente
from produto import Produto
from arranjos import Arranjos
from utilizador import Utilizador 
from utilizador import Login
from datetime import datetime
from calendar import Calendar

class Encomenda():
    lista_encomendas = []
    
    def __init__(self, id_encomenda, utilizador_login, nome_cliente, data_criação, data_entrega, quantidade, preco_total, estado_encomenda):
        self.dados_encomenda = {
            'id' : id_encomenda,
            'login' : utilizador_login,
            'nomeCliente' : nome_cliente,
            'dataCriacao' : data_criação,
            'dataEntrega' : data_entrega,
            'quantidade' : quantidade,
            'precoTotal' : preco_total,
            'estadoEncomenda' : estado_encomenda
        }

    contador_id_encomenda = 1
    def adicionar_encomenda(self):
        id_encomenda = Encomenda.contador_id_encomenda
        Encomenda.contador_id_encomenda +=1  
        
        print(f"Criado por: {Login.acesso['utilizador']}")      

        procurar_cliente = input("Qual é o nome do cliente que deseja fazer a encomenda? ").lower()
        clientes_encontrados = []
        
        for cliente in Cliente.lista_clientes:
            if procurar_cliente == cliente.dados['nome'].lower():
                clientes_encontrados.append(cliente)
            else:
                criar_cliente = input("O cliente não existe, deseja criar um novo? (s/n) ")
                if criar_cliente == "s":
                    Cliente.adicionar_cliente()
                else:
                    return
                
        if len(clientes_encontrados) > 1:
            print("----Clientes Encontrados----")
            for i, cliente in enumerate(clientes_encontrados, start=1):
                print(f"{i}- {cliente.dados['nome']} | contacto: {cliente.dados['contacto']}")
            while True:
                try:
                    escolha_editar = int(input("Qual é que deseja editar? "))
                    cliente = clientes_encontrados[escolha_editar-1]
                    break
                except ValueError:
                    print("Tem de ser um número inteiro, tente novamente!")
                    continue 
        else:
            cliente = clientes_encontrados[0]
             
        if not clientes_encontrados:
            print("Nenhum cliente foi encontrado.")
            return
        
            
       
        while True:
            criar_novo_cliente = input("Deseja criar um novo cliente? (s/n) ").lower()
            
            if criar_novo_cliente == "s":       
                Cliente.adicionar_cliente()
            elif criar_novo_cliente == "n":
                break
            else:
                print("Opção inválida, tente novamente!")
                continue
            

        
      
                    
        print("--Lista de Produtos--")
        for i, produto in enumerate(Produto.lista_produtos, start=1):
           print(f"{i}- {produto} | categoria: {produto.informacoes['categoria']} | subcategoria: {produto.informacoes['subcategoria']} | stock: {produto.informacoes['stock']} | preço: {produto.informacoes['preco']} ")
        while True:
            try:
                escolher_produto = int(input("Escolha o produto que deseja: "))
                if 1 <= escolher_produto <= len(Produto.lista_produtos):
                    produto_escolhido = Produto.lista_produtos[escolher_produto-1]
                    print(f"Escolheu: {produto_escolhido}")
                    break
                else:
                    print(f"Opção inválida. Tem de ser entre 1 e {len(Produto.lista_produtos)}")
            except ValueError:
                print("Tem de ser um número inteiro. Tente novamente!")
                continue

              
        self.dados_encomenda['data_entrega'] = input("Dia para entregar a encomenda: ")
        
        print("Qual é o tipo de encomenda que quer? ")
        for i, arranjos in enumerate(Arranjos.lista_arranjos, start=1):
            print(f"{i}- {arranjos} | limite: {Arranjos.dados_arranjo['limite']}")
        while True:
            try:
                escolha_arranjo = int(input("Escolha o arranjo pelo número: "))
                if 1 <= escolha_arranjo <= len(Arranjos.lista_arranjos):
                    arranjo_escolhido = Arranjos.lista_arranjos[escolha_arranjo-1]
                    print(f"Escolheu: {arranjo_escolhido}")
                    break
            except ValueError:
                print("Tem de ser um número inteiro. Tente novamente!")
                continue
        arranjo_escolhido = Arranjos.lista_arranjos[escolha_arranjo-1]
            
            
    def mostrar_encomendas(self):
        if not Encomenda.lista_encomendas:
            print("Não existem encomendass para mostrar.")
            return
        
        for encomenda in Encomenda.lista_encomendas:
            print(f"ID: {encomenda.dados_encomenda['id']}")
            print(f"Login: {encomenda.dados_encomenda['login']}")
            print(f"Nome do cliente: {encomenda.dados_encomenda['nomeCliente']}")
            print(f"Data da criação da encomenda: {encomenda.dados_encomenda['dataCriação']}")
            print(f"Data para entregar a encomenda: {encomenda.dados_encomenda['dataEntrega']}")
            print(f"Quantidade de produtos: {encomenda.dados_encomenda['quantidade']}")
            print(f"Preço total: {encomenda.dados_encomenda['precoTotal']}")
            print(f"Estado da encomenda: {encomenda.dados_encomenda['estadoEncomenda']}")
            print("-----------------------------------")

    def editar_encomenda(self):
        encomendas_encontradas = []
        
        procurar_encomenda_editar = input("Escreva o nome do cliente que fez a encomenda: ").lower()
        
        for cliente in Cliente.lista_clientes():
            if procurar_encomenda_editar == cliente.dados['nome']:
                for i, cliente in enumerate(encomendas_encontradas, start=1):
                    print(f"{i}- ID:{cliente.dados['id']} | Nome: {cliente.dados['nome']} | Contacto: {cliente.dados['contacto']}\n")
                    print("----informações encomenda----\n ")
                    print(f"{encomenda.dados_encomenda['id']} | Data da criação: {encomenda.dados_encomenda['dataCriacao']} | Data de Entrega: {encomenda.dados_encomenda['dataEntrega']} \n")
                    print(f" | Quantidade: {encomenda.dados_encomenda['quantidade']} | Preço total: {encomenda.dados_encomenda['precoTotal']}€ | Estado da encomenda: {encomenda.dados_encomenda['estadoEncomenda']} ")
        
        
        
        
          
encomenda = Encomenda("", "", "", "", "", "", "")
encomenda.adicionar_encomenda()