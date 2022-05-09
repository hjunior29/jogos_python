print("********************************")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("********************************")

numero_secreto = 9

chute = int(input("Digite o seu número: "))

print ("Você digitou", chute, "\nO número pensado foi", numero_secreto)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou")