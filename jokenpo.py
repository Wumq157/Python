import random

def jogarJokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias = 0
    derrotas = 0
    
    print("Bem-vindo ao jogo.")
    print("Escolha entre: Pedra, Papel ou Tesoura.")

    while True:
        escolhaJogador = input("Qual opção você deseja?").lower()

        if escolhaJogador not in opcoes:
            print("Sua opção é inválida, tente novamente.")
            continue
        
        escolhaPc = random.choice(opcoes)
        print(f"O Computador escolheu: {escolhaPc}")

        if escolhaJogador == escolhaPc:
            print("O jogo empatou")
        elif (
            (escolhaJogador == "pedra" and escolhaPc == "tesoura") or
            (escolhaJogador == "tesoura" and escolhaPc == "papel") or
            (escolhaJogador == "papel" and escolhaPc == "pedra")
            ):
            vitorias += 1
            print("Você ganhou.")
        else:
            derrotas += 1
            print("Você perdeu!!! Hhahahha")
        
        total_jogos = vitorias + derrotas
        if total_jogos > 0:
            win_rate = vitorias / total_jogos * 100
        else:
            win_rate = 0
        
        print(f"Você já ganhou {vitorias} e perdeu {derrotas} está com {win_rate:.2f}% de WinRate")
        jogarNovamente = input(f"Quer jogar novamente? Sim ou Não?").lower()

        if jogarNovamente == "sim":
            continue
        else:
            break

if __name__ == "__main__":
    jogarJokenpo()
