import getpass

class Utilizador():
    def __init__(self, utilizador, palavra_passe):
        self.utilizador = utilizador
        self.palavra_passe = palavra_passe

class Login(Utilizador):
    def __init__(self):
        self.utilizador = {
            'admin' : 'admin123', 'papel' : 'chefe',
            'funcionario' : 'funcionario123', 'papel' : 'funcionario'
        }
       
       
    def verificar_dados(self):
        tentativas = 0
        acesso = False
        while tentativas < 3 and not acesso:
            username = input("Utilizador: ")
            palavra_passe = getpass.getpass("Palavra-passe: ")
            #print(f"DEBUG - username: '{username}', palavra-passe: '{palavra_passe}'")

            if username in self.utilizador and palavra_passe == self.utilizador[username]:
                print("Os dados estão corretos. Seja bem-vindo!")
                acesso = True
                return {'utilizador' : username}
            else:
                tentativas += 1
                tentativas_restantes = 3 - tentativas 
                print(f"Os dados estão errados! Tem mais {tentativas_restantes} tentativas.")

        print("Já chegou no limite de tentativas! Acesso bloqueado.")
        return  


login = Login()
acesso = login.verificar_dados()

if acesso:
    print(f"O acesso foi permitido ao utilizador: {acesso['utilizador']}")
else:
    print("Acesso negado. O programa vai fechar...")

