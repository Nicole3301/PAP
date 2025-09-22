
class Funcionario():
    lista_funcionarios = []
    lista_genero = ["feminino", "masculino"]
    
    def __init__(self, id_funcionario, nome_funcionario, palavra_passe, genero_funcionario, funcao):
        self.Id_funcionario = id_funcionario
        self.Nome_funcionario = nome_funcionario
        self.Palavra_passe = palavra_passe
        self.Genero_funcionario = genero_funcionario
        self.Funcao = funcao
       
    contador_id_funcionario = 1
    def adicionar_funcionario(self):
        id_funcionario = Funcionario.contador_id_funcionario
        Funcionario.contador_id_funcionario +=1
        
        nome_funcionario = input("Nome do funcionário: ").lower()
        
        palavra_passe = input("Palavra-passe: ")
        
        for i, genero in enumerate(Funcionario.lista_genero, start=1):
                print(f"{i}- {genero}")
        while True: 
            try:
                escolha_genero = int(input("Insira o número do gênero: "))
                break
            except ValueError:
                print("A escolha do gênero tem de ser com números inteiros, tente novamente!")
                continue
        genero_funcionario = Funcionario.lista_genero[escolha_genero-1]
    
                   
        funcao = input("Função: ").lower()
        
        novo_funcionario = Funcionario(id_funcionario, nome_funcionario, palavra_passe, genero_funcionario, funcao)
        Funcionario.lista_funcionarios.append(novo_funcionario)
        
        while True:
            ver_dados = str(input("Deseja ver os dados do funcionário? (s/n) ")).lower()
            
            if ver_dados == "s":
                print("---- Dados do Funcionário ----")
                print(f"ID: {novo_funcionario.Id_funcionario}")
                print(f"Nome: {novo_funcionario.Nome_funcionario}")
                print(f"Palavra-passe: {novo_funcionario.Palavra_passe}")
                print(f"Gênero: {novo_funcionario.Genero_funcionario}")
                print(f"Função: {novo_funcionario.Funcao}")
                print("-----------------------------------")
                break
            elif ver_dados == "n":
                break
            else:
                print("Opção inválida! Use 's' ou 'n'. ") 
                continue
        
        while True:       
            try:    
                editar_novamente = input("Gostava de adicionar outro funcionário? (s/n) ").lower()
                if editar_novamente == "s":  
                    funcionario.adicionar_funcionario()
                elif editar_novamente == "n":
                    break
            except ValueError:
                print("Opção inválida! Use 's' ou 'n'. ")    
                continue
                
    def mostrar_dados_funcionarios(self):
        if not Funcionario.lista_funcionarios:
            print("Não existem clientes para mostrar.")
            return
        print("-------- Lista de Funcionários ---------")
        for funcionario in Funcionario.lista_funcionarios:
            print(f"ID: {funcionario.Id_funcionario}")
            print(f"Nome: {funcionario.Nome_funcionario}")
            print(f"Nome: {funcionario.Palavra_passe}")
            print(f"Gênero: {funcionario.Genero_funcionario}")
            print(f"Função: {funcionario.Funcao}")
            print("-----------------------------------")

    def editar_dados_funcionario(self):
        procurar_funcionario_editar = input("Escreva o nome do funcionário que quer editar: ").lower()
        funcionarios_encontrados = []
        
        for funcionario in Funcionario.lista_funcionarios:
            if procurar_funcionario_editar in funcionario.Nome_funcionario.lower():
                funcionarios_encontrados.append(funcionario)    
        
        if not funcionarios_encontrados:
            print("Nenhum funcionário foi encontrado.")
            return
        

        if len(funcionarios_encontrados) > 1:
            for i, funcionario in enumerate(funcionarios_encontrados, start=1):
                print(f"{i}- {funcionario.Nome_funcionario} | Gênero:  {funcionario.Genero_funcionario} | Função: {funcionario.Funcao}")
            escolha_funcionario = int(input("Insira o número do funcionário que deseja editar? "))
            funcionario = funcionarios_encontrados[escolha_funcionario-1]
        else:
            funcionario = funcionarios_encontrados[0]
                
        
        alterar_campo_funcionario = input("Deseja editar o Nome, Palavra-passe ou a Função? ").lower()
        if alterar_campo_funcionario == "nome":
            while True:
                novo_campo = input("Novo nome do funcionário: ").lower()
                funcionarios_duplicados = False
                if funcionarios_duplicados:
                    opcao = input("Já existe um funcionário com esse nome deseja adicionar mesmo assim? (s/n) ")
                    if opcao == "s":
                        self.adicionar_funcionario
                    elif opcao == "n":
                        break
                    else:
                        print("Opção inválida, tente novamente!")
                        return
            funcionario.Nome_funcionario = novo_campo
        elif alterar_campo_funcionario in ["palavrapasse", "palavra_passe", "palavra-passe"]:
            novo_campo = input("Nova palavra-passe: ")
            funcionario.Palavra_passe = novo_campo
        elif alterar_campo_funcionario in ["funcao", "função", "funçao", "funcão"]:
            novo_campo = input("Nova função: ").lower()
            funcionario.Funcao = novo_campo
        else:
            print("Opção inválida, tente novamente!")
            return
        
        print("Os dados foram atualizados!")
        
        
        pergunta = input("Deseja ver os dados que foram atualizados? (s/n) ").lower()
            
        if pergunta == "s":
            self.mostrar_dados_funcionario()
        elif pergunta == "n":
            return    
        else:
            print("Escolha inválida. Tente novamente.")
            
    def remover_funcionario(self):
        nome_funcionario_remover = input("Qual é o nome do funcionário que deseja remover? ").lower()
        lista_funcionarios_encontrados = []
        
        for funcionario in Funcionario.lista_funcionarios:
            if nome_funcionario_remover == Funcionario.lista_funcionarios:
                lista_funcionarios_encontrados.append(funcionario)
        
        if not lista_funcionarios_encontrados:
            print("Nenhum funcionário foi encontrado.")
            return
        
        if len(lista_funcionarios_encontrados) > 1:
            for i, funcionario in enumerate(lista_funcionarios_encontrados, start=1):
                print(f"{i}- {funcionario.Nome_funcionario} | Gênero:  {funcionario.Genero_funcionario} | Função: {funcionario.Funcao}")
            while True:
                try:
                    escolha_funcionario_remover = int(input("Insira o número do funcionário que deseja remover: "))
                    break
                except:
                    print("Tem de ser um número inteiro, tente novamente!")
                    return
            funcionario = lista_funcionarios_encontrados(escolha_funcionario_remover-1)
        else:
            funcionario = lista_funcionarios_encontrados[0]
        
        Funcionario.lista_funcionarios.remove(funcionario)
        print(f"O funcionário com o id {funcionario.Id_funcionario} com o nome {funcionario.Nome_funcionario}  e a função {funcionario.Funcao} foi removido com sucesso.")
        
funcionario = Funcionario("", "", "", "", "")
funcionario.adicionar_funcionario()
funcionario.editar_dados_funcionario()
funcionario.mostrar_dados_funcionarios()
funcionario.remover_funcionario()

        
        