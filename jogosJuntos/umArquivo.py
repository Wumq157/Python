import random

def jogarFo():
    secreta = "viado"
    letrasAcertadas = ["_", "_", "_", "_", "_"]
    tentativas = 7

    while tentativas > 0 and "_" in letrasAcertadas:
        palpite = input("Escreva uma letra:").lower()

        if palpite in secreta:
            index = 0
            for letra in secreta:
                if palpite == letra:
                    letrasAcertadas[index] = letra
                index += 1
        else:
            tentativas -= 1
            print(f"Você errou, ainda tem {tentativas} Restantes.")
        print(f"Você acertou uma das letras: {' '.join(letrasAcertadas)}")

    if "_" not in letrasAcertadas:
        print("Parabéns, você ganhou!")
    else:
        print(f"Que pena, você perdeu. A palavra era {secreta}")

def jogarAd():
    def dificuldade():
        print("Temos 3 tipos de dificuldade além da personalizada.")
        print("Dificuldade (1) Temos que acertar um valor de 0 a 10 em 10 tentativas.")
        print("Dificuldade (2) Temos que acertar um valor de 0 a 50 em 7 tentativas.")
        print("Dificuldade (3) Temos que acertar um valor de 0 a 100 em 5 tentativas.")
        print("Dificuldade (4) Você escolhe os valores.")
        dificuldade = int(input("Digite a dificuldade que você deseja: "))
        return dificuldade

    def pontuacao(tentativas):
        pontuacaoPor = 1000 / (tentativas - (tentativas // 2))
        return pontuacaoPor

    dificuldade_escolhida = dificuldade()
    maxTentativas = 10 if dificuldade_escolhida == 1 else 7 if dificuldade_escolhida == 2 else 5 if dificuldade_escolhida == 3 else int(input("Digite o número de tentativas desejado: "))
    maxNumero = 10 if dificuldade_escolhida == 1 else 50 if dificuldade_escolhida == 2 else 100 if dificuldade_escolhida == 3 else int(input("Digite o número máximo que será sorteado: "))
    tentativas = 0
    pontuacaoPorTentativa = pontuacao(maxTentativas)
    pontuacaoAtual = 1000

    numero = random.randint(1, maxNumero)

    while tentativas < maxTentativas:
        tentativas += 1
        tentativasRestantes = maxTentativas - tentativas
        pontuacaoAtual -= pontuacaoPorTentativa
        numeroEscolhido = int(input(f"Escolha um número entre 0 e {maxNumero}: "))

        if numeroEscolhido == numero:
            print(f"Você acertou o número sorteado em {tentativas} tentativas.")
            print(f"Sua pontuação foi de {pontuacaoAtual} pontos.")
            break
        elif numeroEscolhido > numero:
            print("O número escolhido é maior que o número sorteado.")
            print(f"Você ainda tem {tentativasRestantes} tentativas.")
            print(f"Sua pontuação atual é {pontuacaoAtual}.")
        elif numeroEscolhido < numero:
            print("O número escolhido é menor que o número sorteado.")
            print(f"Você ainda tem {tentativasRestantes} tentativas.")
            print(f"Sua pontuação atual é {pontuacaoAtual}.")
        else:
            print("Algo de errado aconteceu.")

    print("Infelizmente você perdeu. Obrigado por jogar. Tente novamente!")

def escolhaJogo():
    print("----------===========****===========----------")
    print("Escolha seu jogo:")
    print("Digite (1) para forca ou (2) para adivinhar um número.")
    jogo = int(input("Qual jogo você deseja? "))
    if jogo == 1:
        print("Obrigado por jogar nosso jogo da forca.")
        jogarFo()
    elif jogo == 2:
        print("Obrigado por jogar nosso jogo de adivinhação.")
        jogarAd()
    else:
        print("Você digitou um valor inválido.")

escolhaJogo()
