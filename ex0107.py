#crie uma função em Python chamada fibonacci que receba um número inteiro positivo n como parâmetro e exiba os n primeiros termos da
# sequência de Fibonacci.
#A sequência de Fibonacci é formada pela soma dos dois números anteriores, começando com 0 e 1:
from random import randint
princ= []
palpite = int(input('Qual o seu palpite? '))
for i in range(0,palpite):
    jogos = []
    while len(jogos) < 6:
        num = randint(0,60)
        if num not in jogos:
            jogos.append(num)
    jogos.sort()
    princ.append(jogos)
for pos,jogos in enumerate(princ,+1):
    print(f'Jogo: {pos} Número: {jogos}')
print('Voltee SEMPRE')








