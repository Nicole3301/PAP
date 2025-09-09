import getpass

class Utilizador(): 
    def __init__(self, utilizador, palavra_passe, papel):
        self.Utilizador = utilizador
        self.Palavra_passe = palavra_passe
        self.Papel = papel 


class Login(Utilizador):
    def __init__(self):
        self.utilizadores = [
            Utilizador("admin", "admin123", "Administrador"),
            Utilizador("funcionario", "func123", "Funcionário")
        ]
        
    def verificar_dados(self):
        tentativas = 0
        acesso = False
        while tentativas < 3 and not acesso:
            username = input("Utilizador: ")
            palavra_passe = getpass.getpass("Palavra-passe: ")

            for utilizador in self.utilizadores:
                if utilizador.Utilizador == username and utilizador.Palavra_passe == palavra_passe:
                    print("Os dados estão corretos. Seja bem-vindo!")
                    acesso = True
                    return utilizador
            else:
                tentativas += 1
                tentativas_restantes = 3 - tentativas 
                print(f"Os dados estão errados! Tem mais {tentativas_restantes} tentativas.")

        print("Já chegou no limite de tentativas! Acesso bloqueado.")
        return  


login = Login()
acesso = login.verificar_dados()

if acesso:
    print(f"O acesso foi permitido ao utilizador: {acesso.Utilizador}")
else:
    print("Acesso negado. O programa vai fechar...")
