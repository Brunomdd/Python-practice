#Faça um programa que leia tres números e mostre qual é o  maior e qual é o menor
a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
c = int(input('Digite o segundo número:'))
#verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('\033[0;31;31mO menor valor digitado foi {}\033[m'.format(menor))
print('\033[0;34;34mO maior valor digitado foi {}\033[m'.format(maior))