
class Funcionario():
    lista_funcionarios = []
    
    def __init__(self, id_funcionario, nome_funcionario, funcao):
        self.Id_funcionario = id_funcionario
        self.Nome_funcionario = nome_funcionario
        self.Funcao = funcao
       
    contador_id_funcionario = 1
    def adicionar_funcionario(self):
        id_funcionario = Funcionario.contador_id_funcionario
        Funcionario.contador_id_funcionario +=1
        
        while True:
            nome_funcionario = input("Nome do funcionário: ").lower()
            funcionarios_duplicados = False 
            for funcionario in Funcionario.lista_funcionarios:
                if funcionario.Nome_funcionario.lower() == nome_funcionario.lower():
                    funcionarios_duplicados = True
                    break  
            if funcionarios_duplicados:
                opcao = input("Já existe um funcionário com esse nome deseja adicionar mesmo assim? (s/n) ")
                if opcao == "s":
                    self.adicionar_funcionario
                elif opcao == "n":
                    break
                else:
                    print("Opção inválida, tente novamente!")
                    continue
                
                
        funcao = input("Função: ").lower()
        
        novo_funcionario = (id_funcionario, nome_funcionario, funcao)
        Funcionario.lista_funcionarios.append(novo_funcionario)
        
        while True:
            ver_dados_funcionario = str(input("Deseja ver os dados do funcionário que adicionou? (s/n) ")).lower()
            
            if ver_dados_funcionario == "s":
                novo_funcionario.mostrar_dados_funcionario()
            elif ver_dados_funcionario == "n":
                break
            else:
                print("Opção inválida, tente novamente!")
                continue  
            
            
            while True:
                criar_outro_funcionario = str(input("Deseja criar outro funcionário? (s/n) ")).lower()     
                if criar_outro_funcionario == "s":
                    self.adicionar_funcionario
                elif criar_outro_funcionario == "n":
                    break
                else:
                    print("Opção inválida, tente novamente!")
                    continue
                    
                
    def mostrar_dados_funcionario(self):
        if not Funcionario.lista_funcionarios:
            print("Não existe funcionários para mostrar.")
            return
        for funcionario in Funcionario.lista_funcionarios:
            print("---- Lista de Funcionários ----")
            print(f"ID: {funcionario.Id_funcionario}")
            print(f"Nome: {funcionario.Nome_funcionario}")
            print(f"Função: {funcionario.Funcao}")
            print("-----------------------------------")
            
            
    def editar_dados_funcionario(self):
        funcionario_editar = input("Nome do funcionário: ").lower()
        funcionarios_encontrados = []
        
        for funcionario in Funcionario.lista_funcionarios:
            if funcionario_editar in Funcionario.lista_funcionarios:
                funcionarios_encontrados.append(funcionario)
        
        if not funcionarios_encontrados:
            print("Nenhum funcionário foi encontrado.")
            return
        

        if len(funcionarios_encontrados) > 1:
            for i, funcionario in enumerate(funcionarios_encontrados, start=1):
                print(f"{i}- {funcionario.Nome_funcionario} | Função: {funcionario.Funcao}")
            escolha_funcionario = int(input("Insira o número do funcionário que deseja editar? "))
            funcionario = funcionarios_encontrados[escolha_funcionario-1]
        else:
            funcionario = funcionarios_encontrados[0]
                
        
        alterar_campo_funcionario = input("Deseja editar o Nome ou a Função? ").lower()
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
            Funcionario.Nome_funcionario = novo_campo
        elif alterar_campo_funcionario in ["funcao", "função", "funçao", "funcão"]:
            novo_campo = input("Nova função: ").lower()
            Funcionario.Funcao = novo_campo
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
                print(f"{i}- {funcionario.Nome_funcionario} | Função: {funcionario.Funcao}")
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
        print(f"O funcionário com o id {Funcionario.Id_funcionario} com o nome {Funcionario.Nome_funcionario}  e a função {Funcionario.Funcao} foi removido com sucesso.")
        
funcionario = Funcionario("", "", "")
        
        