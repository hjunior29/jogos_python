#importando arquivos
import adivinhacao
import forca

print("********************************")
print("********ESCOLHA UM JOGO*********")
print("********************************")

print("\nAdivinhção (1)\nForca (2)")
jogo = int(input("Escolha um: "))

if jogo == 1:
    print("\nJogando Adivinhação\n\n")
    #chamando o arquivo e chamndo a função do jogo
    adivinhacao.jogar()
if jogo == 2:
    print("\nJogando Forca\n\n")
    #chamando o arquivo e chamndo a função do jogo
    forca.jogar()