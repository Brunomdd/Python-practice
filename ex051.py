from random import randint  # Importa a função randint da biblioteca random, que será usada para gerar a escolha aleatória do computador

# Exibição das opções de escolha para o jogador
print("===================================")
print("JOGO DE JOKENPO (PEDRA-PAPEL-TESOURA)")  # Exibe o título do jogo
print("===================================")
print("-> 1 (PEDRA)")  # Exibe a opção 1 (Pedra)
print("-> 2 (PAPEL)")  # Exibe a opção 2 (Papel)
print("-> 3 (TESOURA)")  # Exibe a opção 3 (Tesoura)
print("-----------------------------------")  # Exibe uma linha para separar a escolha

# Leitura da opção escolhida pelo usuário
opcao = int(input("Escolha uma opção acima: "))  # Solicita ao jogador para digitar uma opção (1, 2 ou 3) e armazena na variável 'opcao'

# Verifica se a opção escolhida pelo jogador é válida (entre 1 e 3)
if opcao >= 1 and opcao <= 3:
    computador = randint(1, 3)  # Gera um número aleatório entre 1 e 3, representando a escolha do computador (1 = Pedra, 2 = Papel, 3 = Tesoura)

    # Exibe a escolha do computador
    if computador == 1:
        print("Computador escolheu (PEDRA)")  # Se o computador escolheu 1 (Pedra), exibe essa opção
    elif computador == 2:
        print("Computador escolheu (PAPEL)")  # Se o computador escolheu 2 (Papel), exibe essa opção
    else:
        print("Computador escolheu (TESOURA)")  # Se o computador escolheu 3 (Tesoura), exibe essa opção

    # Verifica se o jogo é um empate (ambos escolheram a mesma coisa)
    if opcao == computador:
        print("Jogo Empatado")  # Se a escolha do jogador for igual à escolha do computador, é um empate

    else:
        # Verifica as condições de vitória para o jogador
        # Se o jogador escolheu Pedra (1) e o computador escolheu Tesoura (3), o jogador ganhou
        # Se o jogador escolheu Papel (2) e o computador escolheu Pedra (1), o jogador ganhou
        # Se o jogador escolheu Tesoura (3) e o computador escolheu Papel (2), o jogador ganhou
        if (opcao == 1 and computador == 3) or (opcao == 2 and computador == 1) or (opcao == 3 and computador == 2):
            print("Parabéns, você ganhou")  # Se uma das condições acima for verdadeira, o jogador vence
        else:
            print("Computador ganhou")  # Se nenhuma das condições de vitória do jogador for verdadeira, o computador venceu
else:
    print("Opção Inválida")  # Se o jogador escolheu uma opção fora do intervalo 1-3, exibe que a opção é inválida
