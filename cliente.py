class Cliente():
    lista_clientes = []

    def __init__(self, id_cliente, nome_cliente, contacto_cliente):
        self.Id_cliente = id_cliente
        self.Nome_cliente = nome_cliente
        self.Contacto_cliente = contacto_cliente
        
    contador_id = 1
    def adicionar_cliente(self):
        while True: 
            id_cliente = Cliente.contador_id 
            Cliente.contador_id += 1
            nome_cliente = input("Nome: ")
            duplicados = False
            for cliente in Cliente.lista_clientes:
                if cliente.Nome.lower() == nome_cliente.lower():
                    duplicados = True
                    break 
            if duplicados:
                opcao = input("Já existe um cliente com esse nome deseja adicionar mesmo assim? s/n ")
                if opcao == "n":
                    print("Cliente não adicionado, tente outro nome.")
                    continue
                elif opcao != "s":
                    print("Escreva uma opção válida!")
                    continue

            while True:
                try:
                    contacto_cliente = int(input("Contacto: "))
                    break
                except:
                    print("O contacto deve ter números inteiros! Tente novamente.")
                    continue

                
            novo_cliente = Cliente(id_cliente, nome_cliente, contacto_cliente)
            Cliente.lista_clientes.append(novo_cliente)

            while True:
                ver_dados = str(input("Deseja ver os dados do cliente? (s/n) ")).lower()

                if ver_dados == "s":
                    novo_cliente.mostrar_todos_clientes()
                    break
                elif ver_dados == "n":
                    break
                else:
                    print("Opção inválida! Use 's' ou 'n'. ")
 
                         
            while True:
                criar_novamente = input("Gostava de adicionar outro cliente? s/n ").lower()

                if criar_novamente == "s":  
                    break
                elif criar_novamente == "n":
                    return
                else: 
                    print("Opção inválida! Use 's' ou 'n'. ")
                


    def mostrar_todos_clientes(self):
        if not Cliente.lista_clientes:
            print("Não existem clientes para mostrar.")
            return
        for cliente in Cliente.lista_clientes:
            print(f"ID: {cliente.Id}")
            print(f"Nome: {cliente.Nome}")
            print(f"Contacto: {cliente.Contacto}")
            print("-----------------------------------")


    def editar_dados_cliente(self):
        while True:
            procurar_cliente_desejado = input("Qual é o nome do cliente que deseja editar? ").lower()
            clientes_encontrados = []

            for cliente in Cliente.lista_clientes:
                if procurar_cliente_desejado in cliente.Nome_cliente.lower():
                    clientes_encontrados.append(cliente)

            if not clientes_encontrados:
                print("Nenhum cliente foi encontrado.")
                return

            if len(clientes_encontrados) > 1:
                for i, cliente in enumerate(clientes_encontrados, start=1):
                    print(f"{i}- id: {cliente.dados['id']} | nome: {cliente.dados['nome']} | contacto: {cliente.dados['contacto']}")
                escolha = int(input("Qual é que deseja editar? "))
                cliente = clientes_encontrados[escolha-1]
            else:
                cliente = clientes_encontrados[0]


            alterar_campo = input(f"Qual campo deseja alterar do cliente chamado {cliente.dados['nome']}? nome/contacto:")
            if alterar_campo in ['nome', 'contacto']:
                novo_dado = input(f"Novo {alterar_campo}: ")
                cliente.dados[alterar_campo] = novo_dado
            
                if alterar_campo == "contacto":
                    try:
                        novo_dado = int(novo_dado)
                    except:
                        print("O contacto deve ter números inteiros.")
                        return

                cliente.dados[alterar_campo] = novo_dado    
                print("Os dados foram atualizados!")
            else:
                print("Campo inválido. tente novamente")
                continue

            pergunta = input("Deseja ver os dados que foram atualizados? (s/n) ").lower()
            
            if pergunta == "s":
                self.mostrar_todos_clientes()
            elif pergunta == "n":
                return    
            else:
                print("Escolha inválida. Tente novamente.")


    def remover_cliente(self):
        nome_cliente_remover = input("Qual é o nome do cliente que deseja remover? ").lower()
        lista_clientes_encontrados = []

        for cliente in Cliente.lista_clientes:
            if nome_cliente_remover in cliente.dados['nome'].lower():
                lista_clientes_encontrados.append(cliente)

        if not lista_clientes_encontrados:
            print("Nenhum cliente foi encontrado.")
            return

        if len(lista_clientes_encontrados) > 1:
            for i, cliente in enumerate(lista_clientes_encontrados, start=1):
                print(f"{i}- id: {cliente.dados['id']} | nome: {cliente.dados['nome']} | contacto: {cliente.dados['contacto']}")
            escolha = int(input("Qual deseja remover? "))
            cliente = lista_clientes_encontrados[escolha-1]
        else:
            cliente = lista_clientes_encontrados[0]
        

        Cliente.lista_clientes.remove(cliente)
        print(f"O cliente com o id {cliente.dados['id']} com o nome {cliente.dados['nome']} foi removido com sucesso.")


cliente = Cliente("", "", "")
cliente.adicionar_cliente()
cliente.mostrar_todos_clientes()
cliente.editar_dados_cliente()


