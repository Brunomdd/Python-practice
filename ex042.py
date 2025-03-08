#Escreva um programa que leia um número qualquer e mostre a tabuada desse
#número, usando a estrutura “para”.
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15

# Solicita ao usuário que digite um número e o armazena na variável 'num'
num = int(input("Digite um número: "))

# Loop 'for' que vai de 1 até 10 (inclusive), para gerar a tabuada do número
for i in range(1, 11):
    # Calcula o resultado da multiplicação do número 'num' pelo valor de 'i'
    res = num * i

    # Exibe o resultado formatado no estilo "num x i = resultado"
    print("{} x {} = {}".format(num, i, res))

