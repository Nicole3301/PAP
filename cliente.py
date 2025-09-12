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
            
            nome_cliente = input("Nome: ")
            
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
                except:
                    print("A escolha do gênero tem de ser com números inteiros, tente novamente!")
                    continue
            genero = cliente.lista_genero[escolha_genero-1]
            

                
            novo_cliente = Cliente(id_cliente, nome_cliente, contacto_cliente, email, morada, genero)
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
            print(f"ID: {self.Id}")
            print(f"Nome: {self.Nome}")
            print(f"Contacto: {self.Contacto}")
            print(f"email: {self.Email}")
            print(f"Morada: {self.Morada}")
            print(f"Género: {self.Genero}")
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
                    print(f"{i}- id: {cliente.Id_cliente} | nome: {cliente.Nome_cliente} | contacto: {cliente.Contacto_cliente}")
                escolha = int(input("Qual é que deseja editar? "))
                cliente = clientes_encontrados[escolha-1]
            else:
                cliente = clientes_encontrados[0]


            alterar_campo = input(f"Qual campo deseja alterar do cliente chamado {cliente.Nome_cliente}? nome/contacto/email/morada:")
            if alterar_campo == "nome":
                while True:
                    novo_dado_cliente = input(f"Novo Nome: ").lower()
                    funcionarios_duplicados = False
                    if funcionarios_duplicados:
                        opcao = input("Já existe um cliente com esse nome deseja adicionar mesmo assim? (s/n) ")
                        if opcao == "s":
                            self.adicionar_cliente
                        elif opcao == "n":
                            break
                        else:
                            print("Opção inválida, tente novamente!")
                            return
                cliente.Nome_cliente = novo_dado_cliente
            elif alterar_campo == "contacto":
                while True:
                    try:
                        novo_dado_cliente = int(input("Novo contacto: "))
                        cliente.Contacto_cliente = novo_dado_cliente
                    except:
                        print("O contacto deve ter números inteiros.")
                        return
            
            else:
                print("Campo inválido. tente novamente")
                continue
            
            print("Os dados foram atualizados!")

            pergunta = input("Deseja ver os dados que foram atualizados? (s/n) ").lower()
            if pergunta == "s":
                self.mostrar_todos_clientes()
            elif pergunta == "n":
                return    
            else:
                print("Escolha inválida. Tente novamente.")


    def remover_cliente(self):
        remover_cliente = input("Deseja procurar pelo Nome/contacto/email? ").lower()
        lista_clientes_encontrados = []
        
        if remover_cliente in ['nome', 'contacto', 'email']:
            for cliente in Cliente.lista_clientes:
                if remover_cliente is None:
                    return
                else:
                    for i, cliente in enumerate(Cliente.lista_clientes, start=1):
                        print(f"{i}- {cliente.Nome_cliente} | contacto: {cliente.Contacto_cliente} | email: {cliente.Email} | morada: {cliente.Morada} | género: {cliente.Genero}")
                    while True:
                        try:
                            escolha_cliente_remover = int(input("Insira o número do cliente que deseja remover: "))
                            cliente = cliente.Nome_cliente[escolha_cliente_remover -1]
                            break
                        except: 
                            print("Tem de inserir um número inteiro, tente novamente!")
                            continue
                        
            for cliente in Cliente.lista_clientes:
                if self.Nome_cliente != None and self.Nome_cliente == "nome":
                    for i, cliente in enumerate(Cliente.lista_clientes, start=1):
                        print(f"{i}- {cliente.Nome_cliente} | contacto: {cliente.Contacto_cliente} | email: {cliente.Email} | morada: {cliente.Morada} | género: {cliente.Genero}")
                    while True:
                        try:
                            escolha_cliente_remover = int(input("Insira o número do cliente que deseja remover: "))
                            cliente = cliente.Nome_cliente[escolha_cliente_remover -1]
                            break
                        except: 
                            print("Tem de inserir um número inteiro, tente novamente!")
                            continue
                elif self.Contacto_cliente != None and self.Contacto_cliente == "contacto":
                    for i, cliente in enumerate(Cliente.lista_clientes, start=1):
                        print(f"{i}- {cliente.Nome_cliente} | contacto: {cliente.Contacto_cliente} | email: {cliente.Email} | morada: {cliente.Morada} | género: {cliente.Genero}")
                    while True:
                        try:
                            escolha_cliente_remover = int(input("Insira o número do cliente que deseja remover: "))
                            cliente = cliente.Contacto_cliente[escolha_cliente_remover -1]   
                            break
                        except: 
                            print("Tem de inserir um número inteiro, tente novamente!")
                            continue
                    
                    
            
        
        for cliente in Cliente.lista_clientes:
            if remover_cliente in cliente.Nome_funcionario.lower():
                lista_clientes_encontrados.append(cliente)

        if not lista_clientes_encontrados:
            print("Nenhum cliente foi encontrado.")
            return

        if len(lista_clientes_encontrados) > 1:
            for i, cliente in enumerate(lista_clientes_encontrados, start=1):
                print(f"{i}- id: {cliente.Id_funcionario} | nome: {cliente.Nome_cliente} | contacto: {cliente.Contacto_cliente}")
            escolha = int(input("Qual deseja remover? "))
            cliente = lista_clientes_encontrados[escolha-1]
        else:
            cliente = lista_clientes_encontrados[0]
        

        Cliente.lista_clientes.remove(cliente)
        print(f"O cliente com o id {cliente.Id_cliente} com o nome {cliente.Nome_cliente} foi removido com sucesso.")


cliente = Cliente("", "", "", "", "", "")
cliente.adicionar_cliente()
cliente.mostrar_todos_clientes()
cliente.editar_dados_cliente()


