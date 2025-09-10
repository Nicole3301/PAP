from produto import Produto

class Arranjos():

    lista_arranjos = []
    flores = []

    def __init__(self, id_arranjo, nome_arranjo, limite):
        self.Id_arranjo = id_arranjo
        self.Nome_arranjo = nome_arranjo
        self.Limite = limite
        
        
    id_arranjo = 1
    def criar_arranjo(self):
        while True:
            id_arranjo = Arranjos.id_arranjo
            Arranjos.id_arranjo += 1

            nome_arranjo = input("Nome do arranjo: ")
            
            try:
                limite = int(input("Limite de flores: "))
            except:
                print("Tem de ser um número inteiro! Tente novamente.")
                continue
            
            novo_arranjo = Arranjos(id_arranjo, nome_arranjo, limite)
            Arranjos.lista_arranjos.append(novo_arranjo)
            print(f"O arranjo chamado {nome_arranjo} com o limite {limite}.")

            outro_arranjo = input("Deseja adicionar outro arranjo? (s/n) ").lower()

            if outro_arranjo == "s":
                continue
            elif outro_arranjo == "n":  
                break
            else:
                print("Opção inválida! Tente novamente.")
                return outro_arranjo

    def mostrar_arranjos(self):
        if not Arranjos.lista_arranjos:
            print("Não existem arranjos para mostrar.")
            return
            
        for arranjo in Arranjos.lista_arranjos:
            print("------ Lista dos Arranjos ------")
            print(f"ID: {arranjo.Id_arranjo}")
            print(f"Nome do arranjo: {arranjo.Nome_arranjo}")
            print(f"Limite: {arranjo.Limite}")
            print("--------------------------------")
            
    def editar_arranjo(self):
        arranjos_encontrados = []
        nome_arranjo = input("Qual é o nome do arranjo que deseja editar? ").lower()

        for arranjo in Arranjos.lista_arranjos:
            if nome_arranjo in arranjo.Nome_arranjo.lower():
                arranjos_encontrados.append(arranjo)
    
        if not arranjos_encontrados:
            print("Nenhum arranjo foi encontrado.")
            return
            
        if len(arranjos_encontrados) > 1: 
            print("----Arranjos Encontrados----")
            for i, arranjo in enumerate(arranjos_encontrados, start=1):
                print(f"{i}- {arranjo.Nome_arranjo} | limite: {arranjo.Limite} ")
            escolha_para_editar = int(input("Qual é que deseja editar? "))
            arranjo = arranjos_encontrados[escolha_para_editar -1]
        else:
            arranjo = arranjos_encontrados[0]

        alterar_informacao_arranjo = input("Deseje alterar o nome ou o limite? ").lower()

        if alterar_informacao_arranjo in ['nome', 'limite']:
            if alterar_informacao_arranjo == "nome":
                nova_informacao = input("Novo nome: ")
            elif alterar_informacao_arranjo == "limite":
                while True: 
                    try:
                        nova_informacao = int(input("Novo limite: "))
                        arranjo.Limite= nova_informacao
                        break
                    except:
                        print("O limite tem de ter um número inteiro! Tente novamente.")
                        continue
            else:
                print("Opção inválida. Tente novamente.")
                return
                
            print("Os dados foram atualizados!")
            return
 
    def remover_arranjo(self):
        arranjo_encontrado = [] 
        remover_arranjo = input("Qual é o nome do arranjo que deseja remover: ").lower()

        for arranjo in Arranjos.lista_arranjos:
            if remover_arranjo in arranjo.Nome_arranjo.lower():
                arranjo_encontrado.append(arranjo)

        if not arranjo_encontrado:
            print("Nenhum arranjo foi encontrado.")
            return

        if len(arranjo_encontrado) > 1: 
            print("Foram encontrados vários com o mesmo nome: ")
            for i, arranjo in enumerate(arranjo_encontrado, start=1):
                print(f"{i}- ID: {arranjo.Id_arranjo}| Nome do arranjo: {arranjo.Nome_arranjo} | limite de flores: {arranjo.Limite} ")
            escolha_para_remover = int(input("Qual é que deseja remover? "))
            arranjo = arranjo_encontrado[escolha_para_remover -1]
        else:
            arranjo = arranjo_encontrado[0]

        Arranjos.lista_arranjos.remove(arranjo)
        print(f"O arranjo com o ID {arranjo.Id_arranjo}, nome {arranjo.Nome_arranjo} com o limite {arranjo.Limite} foi removido com sucesso.")


arranjos = Arranjos("", "", "", "")
arranjos.criar_arranjo()
arranjos.editar_arranjo()