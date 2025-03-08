#Escreva um programa que converta a temperatura digitada em ºC e converta para Fº.
# Solicita ao usuário que digite a temperatura em Celsius e converte para número de ponto flutuante
c = float(input('Digite a temperatura em Cº:'))

# Converte a temperatura de Celsius para Fahrenheit usando a fórmula: F = (C * 1.8) + 32
f = ((1.8 * c) + 32)

# Exibe a temperatura em Celsius e a correspondente em Fahrenheit, formatando a temperatura em Fahrenheit com 2 casas decimais
print('Graus Cº corresponde a {} e em Fº corresponde a {:.2f}º'.format(c, f))
# {:.2f} formata o valor de Fahrenheit para 2 casas decimais.
