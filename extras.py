class Extras():
    lista_extras = []
    
    def __init__(self, id_extras, nome_extras, preco_extras, stock_extras):
        self.Id_extras = id_extras
        self.Nome_extras = nome_extras
        self.Preco_extras = preco_extras
        self.Stock_extras = stock_extras
        
        
    contador_id_extras = 1
    def adicionar_extras(self):
        while True:
            id_extras = Extras.contador_id_extras 
            Extras.contador_id_extras +=1
        
            nome_extras = input("Nome: ")
            duplicados = False
            for extra in Extras.lista_extras:
                if extra.Nome_extras.lower() == nome_extras.lower():
                    duplicados = True
                    break 
            if duplicados:
                opcao = input("Já existe um extra com esse nome deseja adicionar mesmo assim? s/n ")
                if opcao == "n":
                    print("Extra não adicionado, tente outro nome.")
                    continue
                elif opcao != "s":
                    print("Escreva uma opção válida! Tente novamente...")
                    continue

            while True:
                try:
                    preco_extras = float(input("Preço: "))
                    break
                except ValueError:
                    print("Tem de ser um número duas casas decimais, tente novamente!")
                    continue
                
            while True:
                try:
                    stock_extras = int(input("Stock: "))
                    break
                except ValueError:                    
                    print("Tem de ser um número inteiro, tente novamente!") 
                    continue
                
            novo_extra = Extras(id_extras, nome_extras, preco_extras, stock_extras)  
            Extras.lista_extras.append(novo_extra)  
            print(f"O novo extra já foi adicionada com o nome: {nome_extras}, preço: {preco_extras} € e stock: {stock_extras}")
        
            outro_extra = input("Deseja adicionar outro extra? (s/n) ").lower()
        
            if outro_extra == "s":
                continue
            elif outro_extra == "n":
                break
            else:
                print("Opção inválida, tente novamente!")
                return outro_extra
    
    
    def mostrar_extras(self):
        if not Extras.lista_extras:
            print("Não existem extras para mostrar.")
            return
            
        for extra in Extras.lista_extras:
            print("------ Lista dos Extras ------")
            print(f"ID: {extra.Id_extras}")
            print(f"Nome: {extra.Nome_extras}")
            print(f"Preço: {extra.Preco_extras} €")
            print(f"Stock: {extra.Stock_extras} ")
            print("--------------------------------")
            
            
    def editar_extras(self):
        extras_encontrados = []
        procurar_extra = input("Qual é o nome do extra que deseja editar? ").lower() 
        
        for extra in Extras.lista_extras:
           if procurar_extra in extra.Nome_extras.lower():
              extras_encontrados.append(extra)    

        if not extras_encontrados:
            print("Nenhum extra foi encontrado.")
            return
        
        if len(extras_encontrados) == 1:
            extra = extras_encontrados[0]
        else:
            print("----Extras Encontrados----")
            for i, extra in enumerate(extras_encontrados, start=1):
                print(f"{i}- {extra.Nome_extras} | preço: {extra.Preco_extras} € | stock: {extra.Stock_extras}")
            while True:
                try:
                    escolha_editar = int(input("Qual é que deseja editar? "))
                    extra = extras_encontrados[escolha_editar-1]
                    break
                except ValueError:
                    print("Tem de ser um número inteiro, tente novamente!")
                    continue
        
            
        alterar_informacao_extra = input("Deseja alterar o nome, preço ou stock? ").lower()
        
        if alterar_informacao_extra in ['nome', 'preco', 'preço', 'stock']:
            if alterar_informacao_extra == "nome":
                nova_informacao_extra = input("Novo nome: ").lower()
                extra.Nome_extras = nova_informacao_extra
            elif alterar_informacao_extra in ["preco", "preço"]:
                while True: 
                    try:
                        nova_informacao_extra = float(input("Novo preço: "))
                        extra.Preco_extras = nova_informacao_extra
                        break
                    except ValueError:
                        print("Tem de ser um número com duas casas decimais, tente novamente!")
                        continue
            elif alterar_informacao_extra == "stock":
                while True:
                    try:
                        nova_informacao_extra = int(input("Novo stock: "))
                        extra.Stock_extras = nova_informacao_extra
                        break
                    except ValueError:
                        print("O stock tem de ser um número inteiro, tente novamente!")
                        continue
            else:
                print("Opção inválida, tente novamente!")
                return 
            
            print("Os dados foram atualizados!")
            return
                        
                
    def remover_extra(self):
        extras_encontrados = []
        remover_extra = input("Qual é o nome do extra que deseja remover? ").lower()
        
        
        for extra in Extras.lista_extras:
            if remover_extra in extra.Nome_extras.lower():
                extras_encontrados.append(extra)
                
        if not extras_encontrados:
            print("Nenhum extra foi encontrado.")
            return
        
        if len(extras_encontrados) > 1:
            print("----Extras Encontrados----")
            for i, extra in enumerate(extras_encontrados, start=1):
                print(f"{i}- {extra.Nome_extras} | preço: {extra.Preco_extras} € | stock: {extra.Stock_extras}")
            while True:
                try:
                    escolha_remover_extra = int(input("Escolha o extra que deseja remover: "))
                    extra = extras_encontrados[escolha_remover_extra-1]
                except ValueError:
                    print("Escolha inválida tem de ser um número inteiro, tente novamente!")
                    continue
                
        Extras.lista_extras.remove(extra)
        print(f"O extra {extra.Nome_extras}, preço {extra.Preco_extras}€ e com o stock {extra.Stock_extras} foi removido com sucesso.")
        
extras = Extras("", "", "", "") 
extras.adicionar_extras()
extras.editar_extras()
extras.mostrar_extras()
extras.remover_extra()
extras.mostrar_extras()

            
