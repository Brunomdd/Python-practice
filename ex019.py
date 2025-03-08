#Um professor quer sortear un dos seus quadros para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno1 = str(input('Digite o nome do primeiro Aluno: '))
aluno2 =str(input('Digite o nome do Segundo Aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno:'))
aluno4 = str(input('digite o nome do quarto Aluno '))
lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))