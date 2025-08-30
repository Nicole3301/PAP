class Produto():

    lista_produtos = []
    categorias = ["natural", "artificial"]
    subcategorias = ["flores", "plantas"]


    def __init__(self, id_produto, nome_produto, categoria_escolhida, subcategoria_escolhida, stock, preco):
        self.informacoes = {
            'id' : id_produto,
            'nome' : nome_produto,
            'categoria' : categoria_escolhida,
            'subcategoria' : subcategoria_escolhida,
            'stock' : stock,
            'preco' : preco
        }


    contador_id_produto = 1
    def adicionar_produto(self):
        while True:
            id = Produto.contador_id_produto
            Produto.contador_id_produto += 1

            nome = input("Nome da flor ou planta: ")

            for i, categoria in enumerate(Produto.categorias, start=1):
                print(f"{i}- {categoria}")
            escolha_categoria = int(input("Escolha a categoria: "))
            categoria_escolhida = Produto.categorias[escolha_categoria-1]

            
            for i, subcategoria in enumerate(Produto.subcategorias, start=1):
                print(f"{i}- {subcategoria}")
            escolha_subcategoria = int(input("Escolha a subcategoria: "))
            subcategoria_escolhida = Produto.subcategorias[escolha_subcategoria-1]


            duplicados = False
            for produto in Produto.lista_produtos:
                if produto.informacoes['nome'].lower() == nome.lower():
                    duplicados = True
                    break 
            if duplicados:
                opcao = input("Já existe um produto com esse nome deseja adicionar mesmo assim? s/n ")
                if opcao == "n":
                    print("Produto não adicionado, tente outro nome.")
                    continue
                elif opcao != "s":
                    print("Escreva uma opção válida! Tente novamente...")
                    continue   
            
            try:
                stock = int(input("Stock: "))
            except ValueError:
                print("Tem de ser um número inteiro! Tente novamente.")
                continue
            try:
                preco = float(input("Preço: "))
            except ValueError:
                print("Tem de ser um número inteiro ou com duas casas decimais (5 ou 5.99)! Tente novamente...")
                continue
            
            novo_produto = Produto(id, nome, categoria_escolhida, subcategoria_escolhida, stock, preco)
            Produto.lista_produtos.append(novo_produto)

        
            ver_produto = input("Deseja ver as informações do produto que adicionou? s/n ") 

            if ver_produto == "s":
                novo_produto.mostrar_todos_produtos()
            elif ver_produto != "n":
                print("Opção inválida! Use 's' ou 'n'.")
                break

            adicionar_novamente = input("Gostava de adicionar outro produto? s/n ").lower()

            if adicionar_novamente == "s":  
                continue
            elif adicionar_novamente == "n":
                break
            else: 
                print("Opção inválida! Use 's' ou 'n'. ")



    def mostrar_todos_produtos(self):
        if not Produto.lista_produtos:
            print("Não existem produtos para mostrar.")
            return
        
        for produto in Produto.lista_produtos:
            print("------ Lista dos produtos ------")
            print(f"ID: {produto.informacoes['id']}")
            print(f"Nome da flor: {produto.informacoes['nome']}")
            print(f"estilo da flor: {produto.informacoes['categoria']}")
            print(f"Stock: {produto.informacoes['stock']}")
            print(f"Preço: {produto.informacoes['preco']} €")
            print("--------------------------------")



    def editar_produto(self):
        nome_produto = input("Escreva o nome do produto que deseja editar: ").lower()
        produtos_encontrados = []

        
        for produto in Produto.lista_produtos:
            if nome_produto in produto.informacoes['nome'].lower():
                produtos_encontrados.append(produto)

        if not produtos_encontrados:
            print("Nenhum produto foi encontrado.")
            return
            
        if len(produtos_encontrados) == 1:
            produto = produtos_encontrados[0]
        else:
            for i, produto in enumerate(produtos_encontrados, start=1):
                print(f"{i}- {produto.informacoes['nome']} | categoria: {produto.informacoes['categoria']} | preço: {produto.informacoes['preco']} € | stock: {produto.informacoes['stock']}")
            escolha = int(input("O que deseja editar? "))
            produto = produtos_encontrados[escolha-1]
      
        alterar_informacao = input("Deseja alterar a categoria, stock ou preço? ").lower()

        if alterar_informacao in ['categoria', 'stock', 'preço', 'preco']:
            if alterar_informacao == "categoria":
                for i, categoria in enumerate(Produto.categoria, start=1):
                    print(f"{i}- {categoria}")
                opcao_categoria = int(input("Escolha a categoria: "))
                if 1 <= opcao_categoria <= len(Produto.categoria):
                    produto.informacoes['categoria'] = Produto.categoria[opcao_categoria -1]
            elif alterar_informacao == "stock":
                while True:
                    try:
                        novo_stock = int(input("Novo stock: "))
                        produto.informacoes['stock'] = novo_stock
                        break
                    except ValueError:
                        print("O stock tem de ter um número inteiro! Tente novamente.")
                        continue
            elif alterar_informacao in ["preco", "preço"]:
                while True:
                    try:
                        novo_preco = float(input("Novo preço: "))
                        produto.informacoes['preco'] = novo_preco
                        break
                    except ValueError:
                        print("O preço tem de ser ou um número inteiro ou com casas decimais (5 ou 5.99).")            
            else:
                print("Opção inválida! Tente novamente.")
                return

            print("Os dados foram atualizados!")    
            return
                


    def remover_produto(self):
        produto_encontrado = []
        remover_produto = input("Escreva o nome da flor que deseja remover: ").lower()

        for produto in Produto.lista_produtos:
            if remover_produto in produto.informacoes['nome'].lower():
                produto_encontrado.append(produto)

        if not produto_encontrado:
            print("Nenhum produto foi encontrado.")
            return
            
        if len(produto_encontrado) > 1:
            print("Foram encontrados vários produtos com o mesmo nome: ")
            for i, produto in enumerate(produto_encontrado, start=1):
                print(f"{i}- {produto.informacoes['nome']} | categoria: {produto.informacoes['categoria']} | preço: {produto.informacoes['preco']} € | stock: {produto.informacoes['stock']}")
            escolha_remover = int(input("O que deseja remover? "))
            produto = produto_encontrado[escolha_remover -1]
        else:
            produto = produto_encontrado[0]

        Produto.lista_produtos.remove(produto)
        print(f"O produto {produto.informacoes['nome']} da categoria {produto.informacoes['categoria']} foi removido com sucesso.")

     
    def diminiuir_stock(self, quantidade):
        if self.informacoes['stock'] >= quantidade:
            self.informacoes['stock'] -= quantidade
            return True
        else:
            return False


produto1 = Produto("", "", "", "", "", "")
produto1.adicionar_produto()
produto1.editar_produto()
produto1.mostrar_todos_produtos()
produto1.remover_produto()
produto1.mostrar_todos_produtos()
produto1.remover_produto()

