from tkinter import *
import random

def muda_imagem():
    nova_imagem = f"./imgExercicio/{jogada.get()}.png"
    imagem["file"] = nova_imagem



def verifica_jogada():
    listaCPU = ["pedra", "papel", "tesoura"]
    jogadaCPU = random.choice(listaCPU)
    nova_imagemCPU = f"./imgExercicio/{jogadaCPU}.png"
    imagemCPU["file"] = nova_imagemCPU

    if jogada.get() == "Pedra" and imagemCPU["file"] == "./imgExercicio/tesoura.png":
        rotuloResultado["text"] = "VITÓRIA!"
    elif jogada.get() == "Papel" and imagemCPU["file"] == "./imgExercicio/pedra.png":
        rotuloResultado["text"] = "VITÓRIA!"
    elif jogada.get() == "Tesoura" and imagemCPU["file"] == "./imgExercicio/papel.png":
        rotuloResultado["text"] = "VITÓRIA!"
    elif jogada.get() == imagemCPU["file"]:
        rotuloResultado["text"] = "EMPATE!"
    else:
        rotuloResultado["text"] = "DERROTA!"


window = Tk()
window.title("Jogo Jokenpô")
window.geometry("900x600")
window.configure(bg="goldenrod")
jogada = StringVar()
jogada.set("pedra")

container1 = Frame(window, bg="goldenrod", padx=40)
container2 = Frame(window, bg="goldenrod")
container3 = Frame(window, bg="goldenrod")
container1.pack(side=LEFT)
container2.pack(side=LEFT)
container3.pack(side=LEFT)

##########################################################################################################

rotuloEscolha = Label(container1, text="Escolha", bg="goldenrod")
rotuloEscolha.pack()

texto = ["Pedra", "Papel", "Tesoura"]
valor = ["pedra", "papel", "tesoura"]

for i in range(0, 3, 1):
    Radiobutton(container1, indicatoron=False, text=texto[i], value=valor[i], variable=jogada, width=15, anchor="w", bg="moccasin", command=muda_imagem).pack()

##########################################################################################################

rotuloJogada = Label(container2, text="JOGADOR", bg="goldenrod")
rotuloJogada.pack()

imagem = PhotoImage(file="./imgExercicio/pedra.png")
rotuloImagem = Label(container2, image=imagem, bg="goldenrod")
rotuloImagem.pack()

btnJogada = Button(container2, text="JOGAR", command=verifica_jogada, padx=100)
btnJogada.pack()

##########################################################################################################

rotuloJogadaCPU = Label(container3, text="COMPUTADOR", bg="goldenrod")
rotuloJogadaCPU.pack()

imagemCPU = PhotoImage(file="./imgExercicio/vazio.png")
rotuloImagem = Label(container3, image=imagemCPU, bg="goldenrod")
rotuloImagem.pack()

rotuloResultado = Label(container3, text="", bg="goldenrod")
rotuloResultado.pack()

#########################################################################################################

window.mainloop()