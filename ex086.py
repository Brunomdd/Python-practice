#Desenvolva um programa que leia quatro valores pelo teclado e guardo- os em uma tupla. No final,
#Mostre:
#A Quantas vezes aparece a letra 9
#B Em que posição foi digitado o primeiro valor 3
#C Quais foram os números pares

num1 = int(input('Digite um número: '))
num2 = int(input("Digite um número: "))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))
tupla = (num1,num2,num3,num4)
if 3 in tupla:
    print(f'O número 9 apareceu {tupla.count(9)} vezes')
else:
    print('o valor 3 não foi encontrado em nenhuma posição')
print(f'O número 3 apareceu na posição {tupla.index(3)+1}')
for n in tupla:
    if n % 2 == 0:
        print(f'os valores pares digitados foram {n}')







