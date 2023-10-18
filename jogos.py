import forca
import adivinhacao


def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("[1] Forca [2] Adivinhação")

    jogo = int(input("Qual Jogo: "))

    if(jogo == 1):
        print("Jogo Forca")
        forca.jogar()
    elif(jogo == 2 ):
        print("Jogo Adivinhação")
        adivinhacao.jogar()
if(__name__ == "__main__"):
    escolher_jogo()