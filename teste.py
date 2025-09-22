from tkinter import * 

# criação da janela, dar um nome e um tamanho
janela = Tk()
janela.title("BloomStore")
janela.geometry("800x700")  # largura x altura

# texto
#fg = cor do texto | font = a fonte do texto | text = o que queremos por escrito 
#Label vai criar uma caixa de texto para indicar algo como: Login 
label = Label(janela, text="Login", fg="black", font=("Arial", 20))
#ele consegue se mexer para cima e para baixo
label.pack(pady=100)

# Campo para o nome de utilizador
label_nome = Label(janela, text="Nome de utilizador:", font=("Arial", 14))
label_nome.pack(pady=10)

entrada_nome = Entry(janela, font=("Arial", 14))
entrada_nome.pack(pady=10)

# Campo para a palavra-passe
label_pass = Label(janela, text="Palavra-passe:", font=("Arial", 14))
label_pass.pack(pady=10)

entrada_pass = Entry(janela, font=("Arial", 14), show="*")
entrada_pass.pack(pady=10)

#criação de um botão
botao = Button(janela, text="Entrar", font=("Arial", 14))
botao.pack(pady=20)

entrada_util = Label(janela, font=("Arial", 14))
entrada_util.pack(pady=20)



#para iniciar a janela
janela.mainloop()




