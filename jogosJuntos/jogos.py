import forca
import adivinhacao

def escolhaJogo():
    print("----------===========****===========----------")
    print("Escolha seu jogo:")
    print("Digite (1) para forca ou (2) para adivinhar um número.")
    jogo = int(input("Qual jogo você deseja? "))
    if jogo == 1:
        print("Obrigado por jogar nosso jogo da forca.")
        forca.jogarFo()
    elif jogo == 2:
        print("Obrigado por jogar nosso jogo de adivinhação.")
        adivinhacao.jogarAd()
    else:
        print("Você digitou um valor inválido.")

escolhaJogo()