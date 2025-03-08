#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
from math import trunc
num = float(input('Digite um número qualquer: '))
print('O valor digitado foi {} e a porção inteira dele é {}'.format(num,trunc(num)))