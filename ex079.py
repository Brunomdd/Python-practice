# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas.
from random import randint
from time import sleep
total = 0

vitoria = 0
print("\033[32;35m-="*20)
print("\tJOGO DO PAR OU IMPAR")
print("\033[32;35m-="*20)
while True:
    jogador = int(input("Digite um número: "))
    computador = randint(1,10)
    total = jogador + computador

    tipo = ''
    while tipo != 'P' and tipo != 'I':
        tipo = str(input("Digite o tipo [Par ou Impar]")).upper().strip()[0]
        print("RESULTADO . . . ")
        sleep(0.5)
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total: {total}")

    if total % 2 == 0 and tipo =='P' or total % 2 ==1 and tipo == 'I':
        print("voce venceu!!")
        vitoria +=1
    else:
        print("voce perdeu")
        break
    print("VAMOS JOGAR NOVAMENTE...")
print(f"Voce conseguiu vencer {vitoria} vezes")








