#Crie um programa que permita ao usuário gerar uma sequência de números, de acordo com os valores fornecidos:

#O programa deve pedir ao usuário três valores:
#O valor inicial da sequência (início).
#O valor final da sequência (fim).
#O valor do passo, que define o intervalo entre cada número da sequência.
#Com esses valores, o programa deve gerar e exibir todos os números da sequência, começando no valor "início" e indo até o valor "fim" (inclusive), com o intervalo definido pelo valor do "passo".
# Solicita ao usuário o valor de início para a contagem.

i = int(input("Início: "))  # O valor de "i" é o ponto de partida da sequência.
# Solicita ao usuário o valor de fim para a contagem.
f = int(input("FIM"))  # O valor de "f" é o ponto final da sequência.
# Solicita ao usuário o valor do passo, que define o intervalo entre os números.
passo = int(input("Passo: "))  # O valor de "passo" define a diferença entre os números da sequência.

# Laço de repetição que vai de i até f (inclusivo) com o intervalo definido por "passo".
for i in range(i,f+1,passo):  # O range vai de "i" até "f" (inclusive), e "passo" define a distância entre os números.
    print(i)  # Exibe o valor de "i" a cada iteração do laço.
