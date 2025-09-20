#Média de números
#Faça um programa que:
#Receba uma lista de números (até o usuário digitar um número negativo para parar)
#Calcule a média dos números positivos digitados
#Mostre a média


lista= []
soma = 0
cont = 0
while True:
    numeros = int(input('Digite os numeros: '))
    if numeros < 0 :
        break
    soma += numeros
    cont +=1
if cont > 0:
    media = soma/cont
print(f'A média é {media:.2f}')