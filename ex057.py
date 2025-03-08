# Desenvolva um programa que leia o primeiro termo de uma PA e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

# Solicita ao usuário o primeiro termo da progressão aritmética (PA) e converte para inteiro
#pt = int(input('Primeiro termo: '))

# Solicita ao usuário a razão da progressão aritmética e converte para inteiro
#razão = int(input('Razão: '))

# Calcula o décimo termo da progressão, que é o primeiro termo (pt) somado com 9 vezes a razão
# Isso é feito porque a fórmula do n-ésimo termo de uma PA é: pt + (n-1) * razão
#décimo = pt + (10 - 1) * razão

# Inicia um loop para imprimir os 10 primeiros termos da progressão aritmética
# O loop começa no primeiro termo (pt), vai até o décimo termo (décimo+1) e utiliza a razão para o incremento
#for i in range(pt, décimo + 1, razão):
    # Imprime cada termo da progressão aritmética
    #print(i)

    ## segunda forma

# Solicita ao usuário o valor do primeiro termo da progressão aritmética
primeiro = int(input('Primeiro termo: '))

# Solicita ao usuário o valor da razão da progressão aritmética
razão = int(input('Razão: '))

# Laço 'for' que irá iterar 10 vezes (de 0 a 9)
# Cada iteração representa um termo da progressão aritmética
for i in range(0, 10):  # 'range(0, 10)' faz com que c varie de 0 a 9, gerando 10 termos
    # Calcula e imprime o valor de cada termo da progressão aritmética
    # Fórmula da PA: p1 + rz * c
    print('{}'.format(primeiro + razão * i))  # O 'c' vai aumentando a cada iteração e calcula o próximo termo
