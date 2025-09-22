class Cliente():
    lista_clientes = []
    
    lista_genero = ["feminino", "masculino"]

    def __init__(self, id_cliente, nome_cliente, contacto_cliente, email, morada, genero):
        self.Id_cliente = id_cliente
        self.Nome_cliente = nome_cliente
        self.Contacto_cliente = contacto_cliente
        self.Email = email
        self.Morada = morada
        self.Genero = genero
    
    contador_id = 1
    def adicionar_cliente(self):
        while True: 
            id_cliente = Cliente.contador_id 
            Cliente.contador_id += 1
            
            nome_cliente = input("Nome: ").lower()
            
            validar_contacto=True
            while validar_contacto:
                
                contacto_cliente = input("Contacto: ")
                    
                if len(contacto_cliente) == 9:
                    contacto_cliente = int(contacto_cliente)
                    validar_contacto = False
                else:
                    print("O contacto deve ter números inteiros no máximo 9! Tente novamente.")   
                    continue 
                
            email = input("Email: ")
            
            morada = input("Morada: ")
            
            for i, genero in enumerate(Cliente.lista_genero, start=1):
                print(f"{i}- {genero}")
            while True: 
                try:
                    escolha_genero = int(input("Insira o número do gênero: "))
                    break
                except ValueError:
                    print("A escolha do gênero tem de ser com números inteiros, tente novamente!")
                    continue
            genero = Cliente.lista_genero[escolha_genero-1]
            

                
            novo_cliente = Cliente(id_cliente, nome_cliente, contacto_cliente, email, morada, genero)
            Cliente.lista_clientes.append(novo_cliente)

            while True:
                ver_dados = str(input("Deseja ver os dados do cliente? (s/n) ")).lower()

                if ver_dados == "s":
                    print("---- Dados do Cliente ----")
                    print(f"ID: {novo_cliente.Id_cliente}")
                    print(f"Nome: {novo_cliente.Nome_cliente}")
                    print(f"Contacto: {novo_cliente.Contacto_cliente}")
                    print(f"email: {novo_cliente.Email}")
                    print(f"Morada: {novo_cliente.Morada}")
                    print(f"Género: {novo_cliente.Genero}")
                    print("-----------------------------------")
                    break
                elif ver_dados == "n":
                    break
                else:
                    print("Opção inválida! Use 's' ou 'n'. ")
                    continue
 
            while True:
                try:             
                    criar_novamente = input("Gostava de adicionar outro cliente? s/n ").lower()

                    if criar_novamente == "s":  
                        cliente.adicionar_cliente()
                        break
                    elif criar_novamente == "n":
                        break
                except ValueError: 
                    print("Opção inválida! Use 's' ou 'n'. ")
                    continue


    def mostrar_todos_clientes(self):
        if not Cliente.lista_clientes:
            print("Não existem clientes para mostrar.")
            return
        print("-------- Lista de Clientes ---------")
        for cliente in Cliente.lista_clientes:
            print(f"ID: {cliente.Id_cliente}")
            print(f"Nome: {cliente.Nome_cliente}")
            print(f"Contacto: {cliente.Contacto_cliente}")
            print(f"email: {cliente.Email}")
            print(f"Morada: {cliente.Morada}")
            print(f"Género: {cliente.Genero}")
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
                pesquisar_novamente = input("Deseja voltar a pesquisar? (s/n) ").lower()
                tentativas = 0
                while tentativas < 3:
                    if pesquisar_novamente == "s":
                        break
                    elif pesquisar_novamente == "n":
                        adicionar_novo_cliente = (f"Deseja criar um novo cliente? (s/n) ").lower()
                        if adicionar_novo_cliente  == "s":
                            self.adicionar_cliente()
                        elif adicionar_novo_cliente == "n":
                            break
                        else:
                            print("Opção inválida, tente novamente.")
                            continue
                    else:
                        tentativas += 1
                        
                    
                    

            if len(clientes_encontrados) > 1:
                for i, cliente in enumerate(clientes_encontrados, start=1):
                    print(f"{i}- Id: {cliente.Id_cliente} | Nome: {cliente.Nome_cliente} | Contacto: {cliente.Contacto_cliente} | Email: {cliente.Email} |Morada: {cliente.Morada} | Gênero: {cliente.Genero}")
                escolha = int(input("Qual é que deseja editar? "))
                cliente = clientes_encontrados[escolha-1]
            else:
                cliente = clientes_encontrados[0]


            alterar_campo = input(f"Qual campo deseja alterar do cliente chamado {cliente.Nome_cliente} (nome/contacto/email/morada)? ").lower()
            if alterar_campo == "nome":
                while True:
                    nome_antigo = cliente.Nome_cliente
                    novo_dado_cliente = input("Novo nome: ")
                    if novo_dado_cliente == nome_antigo:
                        print("Escreveu o mesmo nome, escreva de forma diferente se quer editar.")
                        editar_novamente = input("Deseja voltar a editar? (s/n) ").lower() 
                        if editar_novamente == "s":  
                            continue
                        elif editar_novamente == "n":
                            return
                        else: 
                            print("Opção inválida! Use 's' ou 'n'. ")
                    else:
                        cliente.Nome_cliente = novo_dado_cliente
                        break 
                    
            elif alterar_campo == "contacto":
                validar_contacto=True
                while validar_contacto:
                    contacto_antigo = cliente.Contacto_cliente
                    novo_dado_cliente = input("Novo contacto: ")
                    
                    if len(novo_dado_cliente) != 9:
                        print("O contacto deve ter números inteiros no máximo 9! Tente novamente.")   
                        continue 

                    if int(novo_dado_cliente) == contacto_antigo:
                        print("Escreveu o mesmo contacto, escreva outro se quer editar.")
                        editar_novamente = input("Deseja voltar a editar? (s/n) ").lower() 
                        if editar_novamente == "s":  
                            return
                        elif editar_novamente == "n":
                            return
                        else: 
                            print("Opção inválida! Use 's' ou 'n'. ")
                            continue
                        
                cliente.Contacto_cliente = novo_dado_cliente
                break 
                  
            elif alterar_campo == "morada":
                while True:
                    morada_antiga = cliente.Morada
                    novo_dado_cliente = input("Nova morada: ")
                    if novo_dado_cliente == morada_antiga:
                        print("Escreveu a mesma morada, escreva outra se quer editar.")
                        editar_novamente = input("Deseja voltar a editar? (s/n) ").lower() 
                        if editar_novamente == "s":  
                            continue
                        elif editar_novamente == "n":
                            return
                        else: 
                            print("Opção inválida! Use 's' ou 'n'. ")
                    else:
                        cliente.Morada = novo_dado_cliente
                        break 
            elif alterar_campo == "email":
                while True:
                    email_antigo = cliente.Email
                    novo_dado_cliente = input("Novo email: ")
                    if novo_dado_cliente == email_antigo:
                        print("Voltou a escrever o mesmo email se quer editar tem de escrever outro email.")
                        editar_novamente = input("Deseja voltar a editar? (s/n) ").lower()
                        if editar_novamente == "s":  
                            continue
                        elif editar_novamente == "n":
                            return
                        else: 
                            print("Opção inválida! Use 's' ou 'n'. ")
                    else:
                        cliente.Email = novo_dado_cliente
                        break
            else:
                print("Campo inválido. tente novamente")
                return
            
            print("Os dados foram atualizados!")
            
            pergunta = input("Deseja ver os dados que foram atualizados? (s/n) ").lower()
            if pergunta == "s":
                self.mostrar_todos_clientes()
            elif pergunta == "n":
                return    
            else:
                print("Escolha inválida. Tente novamente.")
                return
            break

    def remover_cliente(self):
        remover_cliente = input("Escreva o nome do cliente que deseja remover:  ").lower()
        lista_clientes_encontrados = []
        
               
        for cliente in Cliente.lista_clientes:
            if remover_cliente in cliente.Nome_cliente.lower():
                lista_clientes_encontrados.append(cliente)

        if not lista_clientes_encontrados:
            print("Nenhum cliente foi encontrado.")
            return

        if len(lista_clientes_encontrados) > 1:
            for i, cliente in enumerate(lista_clientes_encontrados, start=1):
                print(f"{i}- Id: {cliente.Id_cliente} | Nome: {cliente.Nome_cliente} | Contacto: {cliente.Contacto_cliente} | Email: {cliente.Email} |Morada: {cliente.Morada} | Gênero: {cliente.Genero}")
            escolha = int(input("Qual deseja remover? "))
            cliente = lista_clientes_encontrados[escolha-1]
        else:
            cliente = lista_clientes_encontrados[0]
        

        Cliente.lista_clientes.remove(cliente)
        print(f"O cliente com o id {cliente.Id_cliente} com o nome {cliente.Nome_cliente} com o contacto {cliente.Contacto_cliente} e email {cliente.Email} foi removido com sucesso.")


cliente = Cliente("", "", "", "", "", "")
cliente.adicionar_cliente()
cliente.editar_dados_cliente()
cliente.remover_cliente()



