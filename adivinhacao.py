print("********************************")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("********************************")

#definindo o número secreto
numero_secreto = 9
tentativas = 5

for rodada in range(1, tentativas+1):
    print("\nTentativa: {} de {}".format(rodada, tentativas))
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

    #decremento
    rodada = rodada + 1

print("Fim de jogo!")