import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("[1] Fácil\n[2] Médio\n[3] Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1 ):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    print("*********************************")

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {} ".format(rodada, total_de_tentativas))
        chute_str = input("Digite o número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100 ):
            print("Número inválido! Digite número entre 1 e 100: ")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou! Sua pontuação é {} pontos!".format(pontos))

            break
        else:
            if (maior):
                print("Você errou! O chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Número secreto é: ", numero_secreto)
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
