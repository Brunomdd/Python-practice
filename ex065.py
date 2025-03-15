# melhore o jogo do DESAFIO 028 onde o computador vai "pensar em um número entre 0 e 10."
# só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# Importando a função 'randint' da biblioteca 'random', que gera números aleatórios
#from random import randint

# Inicializando a variável 'cont' para contar o número de tentativas
#cont = 0

# Gerando um número aleatório entre 1 e 10 (inclusive) para o computador
#computador = randint(1, 11)

# Exibindo uma mensagem inicial para o jogador, pedindo para ele deixar o palpite
#print("======== Deixe seu palpite ========")

# Iniciando o laço de repetição que continuará até o jogador acertar o número
#while True:
    # Solicitando ao jogador que insira um palpite (um número entre 1 e 10)
 #   jogador = int(input("Em que número eu pensei? [Entre 1 e 10]:"))

    # Incrementando o número de tentativas a cada palpite
  #  cont += 1

    # Verificando se o palpite do jogador é igual ao número escolhido pelo computador
  #  if jogador == computador:
        # Exibindo o número que o computador pensou
     #   print("o número do computador era {}".format(computador))

        # Parabenizando o jogador e informando quantas tentativas ele precisou
      #  print(f'Parábens voce acertou, mas voce precisou de {cont} tentativas para vencer')

        # Encerra o laço, já que o jogador acertou
      #  break

# Segundo método de resolução

# Inicializando a variável 'palpite' para contar o número de tentativas
palpite = 0

# Importando a função 'randint' da biblioteca 'random', que gera números aleatórios
from random import randint

# Gerando um número aleatório entre 1 e 10 (inclusive) para o computador
computador = randint(1, 11)

# Exibindo uma mensagem inicial para o jogador, explicando o jogo
print("sou seu computador acabei de pensar em um número entre 0 e 10")
print("voce consegue adivinhar qual foi?")

# Inicializando a variável 'acertou' como False, indicando que o jogador ainda não acertou
acertou = False

# Iniciando o laço while que continuará até que o jogador acerte o número
while not acertou:
    # Solicita um palpite do jogador e converte para inteiro
    jogador = int(input("Qual é o seu palpite? "))

    # Incrementa o número de palpites feitos
    palpite += 1

    # Verifica se o palpite do jogador é igual ao número do computador
    if jogador == computador:
        acertou = True  # Se o jogador acertou, a variável 'acertou' é definida como True, e o loop termina
    else:
        # Se o palpite for menor que o número do computador, o programa dá a dica "Mais.."
        if jogador < computador:
            print("Mais..Tente mais uma vez")
        # Se o palpite for maior que o número do computador, o programa dá a dica "Menos.."
        elif jogador > computador:
            print("Menos.. Tente mais uma vez")

# Quando o jogador acerta, exibe a mensagem de vitória com o número de tentativas feitas
print(f"Parabens ! Voce precisou de {palpite} palpites para vencer")




