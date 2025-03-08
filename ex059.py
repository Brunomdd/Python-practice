# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de tres e que se encontram no intervalo de 1 até 500
cont = 0  # Contador de números ímpares múltiplos de 3
soma = 0  # Soma de números ímpares múltiplos de 3

# Percorrendo apenas números ímpares de 1 até 500
for i in range(1, 501, 2):  # Garante que só serão percorridos números ímpares
    if i % 3 == 0:  # Verifica se o número é múltiplo de 3
        soma += i  # Adiciona o número à soma
        cont += 1  # Incrementa o contador

# Exibe o resultado
print('A soma de todos os {} números múltiplos de 3 é {}.'.format(cont,soma))