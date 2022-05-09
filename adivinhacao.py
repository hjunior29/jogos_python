def jogar():
    #importando biblioteca
    import random

    print("********************************")
    print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
    print("********************************")

    #escolhendo o nível
    print("Qual nível de dificuldade?")
    print("Fácil (1)\nMédio (2)\nDifícil (3)")
    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        tentativas = 15
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    else:
        print("Nível inválido")
        tentativas = 0

    #sorteando o número secreto
    #--numero_secreto = round((random.random()*100))
    numero_secreto = random.randrange(1, 100)

    #pontuação
    pontos = 1000

    for rodada in range(1, tentativas+1):
        print(f"\nTentativa: {rodada} de {tentativas}")
        chute = int(input("Digite o seu número: "))
        if chute < 1 or chute > 100:
            print("Você deve escolher um valor entre 1 e 100")
            continue

        #testes
        igual = chute == numero_secreto
        maior = chute < numero_secreto
        menor = chute > numero_secreto

        #condicoes
        if igual:
            print("Você acertou!")
            break
        else:
            if menor:
                print("Você errou!! O número secreto é MENOR que o número que você chutou")
            elif maior:
                print("Você errou!! O número secreto é MAIOR que o número que você chutou")

            #pontuação
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        #decremento
        rodada = rodada + 1

    print(f"\nNúmero escolhido: {numero_secreto}")
    print(f"Sua pontuação: {pontos}")
    print("Fim de jogo!")