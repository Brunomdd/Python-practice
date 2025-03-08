#Faça um programa em Python que abre e reproduza o áudio de mum arquivo mp3
# Importa o módulo pygame, que é uma biblioteca usada para criar jogos e multimídia
import pygame

# Inicializa todos os módulos do Pygame, incluindo o mixer para tocar música
pygame.init()

# Carrega um arquivo de música (neste caso, 'ex021.mp3') para o mixer do Pygame
pygame.mixer.music.load('ex021.mp3')

# Inicia a reprodução da música carregada
pygame.mixer.music.play()

# A função 'input()' faz com que o programa aguarde uma entrada do usuário antes de continuar.
# Isso é usado aqui para garantir que o programa não termine imediatamente enquanto a música ainda está tocando.
input()

# A função 'pygame.event.wait()' faz o programa esperar até que um evento ocorra, como o fechamento da janela.
# Isso mantém o programa em execução, permitindo que a música continue tocando enquanto o script aguarda o fim do evento.
pygame.event.wait()
