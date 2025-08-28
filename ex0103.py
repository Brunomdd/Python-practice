#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
#Quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
sorteios = []
palpites = int(input('Quantos palpites voce quer que eu sorteie?'))
for i in range(1,palpites+1):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            jogo.sort()
    sorteios.append(jogo[:])
print("\nGERANDO OS JOGOS...\n")
sleep(1)
for i, jogo in enumerate(sorteios,+1):
    print(f"Jogo {i}: {jogo}")
    sleep(0.5)

lista = []
jogos = []
from random import randint
from time import sleep
quant = int(input('Quantos jogos voce quer que eu sorteie: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    tot+=1

for v,l in enumerate(jogos):
    print(f'Jogo {v+1}: {l}')
    sleep(1)
print("-="*5, '<BOA SORTE!>','-='*5)















