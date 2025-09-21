#Crie um programa que:
#Peça para o usuário digitar 5 números inteiros.
#Armazene esses números em uma lista.
#Calcule e mostre:
#O maior número digitado.
#O menor número digitado.
#A média dos números.
#Remova o menor número da lista.
#Exiba a lista atualizada, sem o menor número.

numeros = []
maior = 0

menor = 0
s = 0
for i in range(1,6):
    usuarios =int(input(f'Digite o {i} número:'))
    numeros.append(usuarios)
    s += usuarios
maior = numeros[0]
menor = numeros[0]
    
for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor= num
    
print(f'O maior numero é {maior}')
print(f'o menor número é {menor}')
media = s/len(numeros)
print(f'a média é {media:.2f}')

numeros.remove(menor)
print(f'Lista atualizada{numeros} sem o {menor}')
   