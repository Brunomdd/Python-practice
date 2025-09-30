#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: Início, Fim e Passo.
#Seu programa deve realizar três contagens utilizando a função criada:
#A 1 até 10, de 1 em 1
#B  10 até 0 de 2 em 2
#Contagem personalizada
from time import sleep

def contador(i,f,p):
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    print(f'\nContagem de {i} até {f} passo {p}')

    if i <= f:
        while i<= f:
            
            print(f'{i}',end=' ',flush=True)
            sleep(0.2)
            i +=p
    else:
        while i >=f:
            
            print(f'{i}',end=' ',flush=True)
            sleep(0.2)
            i -= p



print()
contador(1,10,1)
contador(10,0,2)
print()
print('Contagem Personalizada: ')
i = int(input('Ìnicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
sleep(0.2)
contador(i,f,p)



