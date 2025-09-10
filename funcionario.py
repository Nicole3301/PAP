
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

            