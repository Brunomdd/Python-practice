#Escreva um programa que faça o computador 'pensar' em um número inteiroo entre
#0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
#computador. o usuario deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

# O computador 'pensa' em um número aleatório entre 0 e 5
computador = randint(0, 5)  # Gera um número aleatório entre 0 e 5

# Exibe uma série de mensagens decorativas para dar uma introdução ao jogo
print('===' * 20)  # Imprime uma linha de "===" repetida 20 vezes para separar visualmente a tela
print('Vou pensar em um número de 0 a 5, tente adivinhar....')  # Informa ao jogador que o computador "pensou" em um número
print('===' * 20)  # Repete a linha de "==="

# O jogador tenta adivinhar o número que o computador pensou
jogador = int(input('Em que número eu pensei ?:'))  # Solicita a entrada do jogador e converte para inteiro

# Exibe a mensagem "PROCESSANDO..." para dar a impressão de que o computador está fazendo algo antes de mostrar o resultado
print('PROCESSANDO. . . .')

# Pausa o programa por 10 segundos para aumentar a tensão do jogo
sleep(10)

# Verifica se o jogador acertou o número que o computador pensou
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer')  # Se o jogador acertou, imprime uma mensagem de vitória
else:
    # Se o jogador errou, revela o número que o computador pensou e o número que o jogador escolheu
    print('Ganhei! Eu pensei no número {} e não no número {}'.format(computador, jogador))

