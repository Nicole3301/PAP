from produto import Produto

class Arranjos():

    lista_arranjos = []
    flores = []

    def __init__(self, id, nome_arranjo, limite):
        self.dados_arranjo = {
            'id' : id,
            'nome' : nome_arranjo,
            'limite' : limite
        }

    id_arranjo = 1
    def criar_arranjo(self):
        while True:
            id = Arranjos.id_arranjo
            Arranjos.id_arranjo += 1

            nome_arranjo = input("Nome do arranjo: ")
            
            try:
                limite = int(input("Limite de flores: "))
            except ValueError:
                print("Tem de ser um número inteiro! Tente novamente.")
                continue
            
            novo_arranjo = Arranjos(id, nome_arranjo, limite)
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
            print(f"ID: {arranjo.dados_arranjos['id']}")
            print(f"Nome da flor: {arranjo.dados_arranjos['nome']}")
            print(f"estilo da flor: {arranjo.dados_arranjos['limite']}")
            print("--------------------------------")
            
    def editar_arranjo(self):
        arranjos_encontrados = []
        nome_arranjo = input("Qual é o nome do arranjo que deseja editar? ").lower()

        for arranjo in Arranjos.lista_arranjos:
            if nome_arranjo in arranjo.dados_arranjo['nome'].lower():
                arranjos_encontrados.append(arranjo)
    
        if not arranjos_encontrados:
            print("Nenhum arranjo foi encontrado.")
            return
            
        if len(arranjos_encontrados) > 1: 
            print("----Arranjos Encontrados----")
            for i, arranjo in enumerate(arranjos_encontrados, start=1):
                print(f"{i}- {arranjo.dados_arranjo['nome']} | limite: {arranjo.dados_arranjo['limite']} ")
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
                        arranjo.dados_arranjo['limite'] = nova_informacao
                        break
                    except ValueError:
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
            if remover_arranjo in arranjo.dados_arranjo['nome'].lower():
                arranjo_encontrado.append(arranjo)

        if not arranjo_encontrado:
            print("Nenhum arranjo foi encontrado.")
            return

        if len(arranjo_encontrado) > 1: 
            print("Foram encontrados vários com o mesmo nome: ")
            for i, arranjo in enumerate(arranjo_encontrado, start=1):
                print(f"{i}- {arranjo.dados_arranjo['nome']} | limite: {arranjo.dados_arranjo['limite']} ")
            escolha_para_remover = int(input("Qual é que deseja remover? "))
            arranjo = arranjo_encontrado[escolha_para_remover -1]
        else:
            arranjo = arranjo_encontrado[0]

        Arranjos.lista_arranjos.remove(arranjo)
        print(f"O arranjo {arranjo.dados_arranjo['nome']} com o limite {arranjo.dados_arranjo['limite']} foi removido com sucesso.")


arranjos = Arranjos("","", "")
arranjos.criar_arranjo()
arranjos.editar_arranjo()