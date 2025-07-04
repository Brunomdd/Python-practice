#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
num1 = randint(0,10)
num2 =randint(0,10)
num3 = randint(0,10)
num4= randint(0,10)
num5= randint(0,10)
tupla = (num1,num2,num3,num4,num5)
print(f'os números sorteados foram {tupla}')
print(f'O maior valor foi {max(tupla)}')
print(f'O menor  valor foi {min(tupla)}')