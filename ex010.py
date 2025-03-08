#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos dolares ela pode comprar.

# Solicita ao usuário que informe o valor de dinheiro que ele tem na carteira
real = float(input('Quanto dinheiro você tem na carteira? '))

# Calcula o valor correspondente em dólares (considerando que 1 dólar = 5.60 reais)
dolar = real / 5.60

# Exibe o valor em reais e o valor correspondente em dólares, formatando ambos com 2 casas decimais
print('Com R${:.2f} você pode comprar {:.2f} US$'.format(real, dolar))
# A função 'format()' substitui as chaves {} pelos valores de 'real' e 'dolar'.
# {:.2f} é usado para formatar os valores para 2 casas decimais.
