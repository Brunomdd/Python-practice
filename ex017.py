#Faça um programa que leia o comprimento do cateto oposto e do cateto Adjacente
#de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
x = float(input('Comprimento do Cateto Oposto: '))
y = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = hypot(x,y)
print('A hipotenusa com catetos {} e {} é igual a {:.2f}'.format(x,y,hipotenusa))
