#Crie um programa que solicite ao usuário a digitação de um número inteiro e, em seguida,
# exiba a tabuada desse número de 1 a 10.

# Inicia a variável cont com o valor 1. Ela será usada como contador para a tabuada.
cont = 1

# Solicita ao usuário que digite um número e o converte para um valor inteiro.
num = int(input("Digite um número: "))

# Inicia um loop que irá rodar enquanto a variável cont for menor ou igual a 10.
while cont <= 10:
    # Calcula o resultado da multiplicação entre o número inserido pelo usuário e o valor do contador.
    res = num * cont

    # Exibe o resultado da multiplicação no formato "num x cont = res".
    print("{} x {} = {}".format(num, cont, res))

    # Incrementa a variável cont em 1, para passar para o próximo valor da tabuada.
    cont = cont + 1





