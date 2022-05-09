print("********************************")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("********************************")

#definindo o número secreto
numero_secreto = 9

chute = int(input("Digite o seu número: "))

#print ("Você digitou", chute, "\nO número pensado foi", numero_secreto)

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

print("Fim de jogo!")