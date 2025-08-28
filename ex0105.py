#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
#Retangular(largura e comprimento) e mostre a área do terreno.

def area(largura,comprimento):

    terreno = largura*comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {terreno}m²')

print('Controle de terrenos')
print('='*20)
a = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
area(a,c)


