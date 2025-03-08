# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10
#até 0, com uma pausa de 1 segundo entre eles.

# Importa a função 'sleep' do módulo 'time' para permitir pausas entre as impressões
from time import sleep

# Importa a função 'emojize' do módulo 'emoji', que converte strings de emojis em emojis reais
from emoji import emojize

# Inicia um loop que vai de 10 até 0, com decremento de 1 a cada iteração
for i in range(10, -1, -1):
    # Imprime o número atual de i
    print(i)
    # Faz uma pausa de 1 segundo antes de continuar para a próxima iteração
    sleep(1)

# Após o loop, imprime a mensagem "ACABOU!" com emojis de fogos de artifício e fogo
print(emojize("ACABOU!:fireworks::fire:"))
# 'emojize()' converte o texto ':fireworks:' e ':fire:' para os respectivos emojis.

