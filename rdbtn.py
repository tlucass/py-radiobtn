from tkinter import *

def muda_imagem():
    nova_imagem = "./imagens/" + escolha.get() + ".png"
    imagem["file"] = nova_imagem

window = Tk()
window.title("Escolha seu avatar")
window.geometry("400x300")
window.configure(bg="moccasin")
escolha = StringVar()
escolha.set("chaplin")
container1 = Frame(window, padx=40, bg="moccasin")
container2 = Frame(window, pady=80, bg="moccasin")
container1.pack(side=LEFT)
container2.pack(side=TOP)

texto = ["Charles Chaplin", "Harley Quinn", "Ninja do Deserto", "Copo do Zorro"]
valor = ["chaplin", "arlequina", "ninja", "zorro"]

for i in range(0, 4, 1):
    Radiobutton(container1, indicatoron=False, text=texto[i], value=valor[i], variable=escolha, width=15, anchor="w", padx=10, pady=5, bg="moccasin", command=muda_imagem).pack()


imagem = PhotoImage(file="./imagens/chaplin.png")
rotuloImagem = Label(container2, image=imagem, bg="moccasin")
rotuloImagem.pack()


window.mainloop()