#xercício: Remover elementos duplicados
#Faça um programa que:
#Peça para o usuário digitar 10 números inteiros, armazenando-os numa lista.
#Crie uma nova lista que contenha apenas os números únicos da lista original (sem duplicatas).
#Mostre a lista original e a lista sem duplicatas.


lista = []
unicos = []
for i in range(1,11):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
    if numeros  not in unicos:
        unicos.append(numeros)

print(f'lista original: {lista}')
print(f'Lista sem duplicadas {unicos}')