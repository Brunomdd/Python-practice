#Desenvolva um programa que leia o comprimento de tres retas
#e diga ao usuário se elas podem ou não formar um triãngulo.
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo seguimento:'))
r3 = float(input('Terceiro seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O seguimentos formam um TRIANGULO!')
else:
    print('Os Seguimentos não podem formar um TRIANGULO!')