print("********************************")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("********************************")

#definindo o número secreto
numero_secreto = 9
tentativas = 5
rodada = 1

while (rodada <= tentativas):
    print("\nTentativa: {} de {}".format(rodada, tentativas))
    chute = int(input("Digite o seu número: "))

    #testes
    igual = chute == numero_secreto
    maior = chute < numero_secreto
    menor = chute > numero_secreto

    #condicoes
    if (igual):
        print("Você acertou!")
    else:
        if (menor):
            print("Você errou!! O número secreto é MENOR que o número que você chutou")
        elif (maior):
            print("Você errou!! O número secreto é MAIOR que o número que você chutou")

    #decremento
    rodada = rodada + 1

print("Fim de jogo!")