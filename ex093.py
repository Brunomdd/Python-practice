# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre - os em uma lista, já na posição correta da inserção (sem usar o sort)
#No final, mostre a lista ordenada na tela.
lista = []
cont = 0
for i in range(0,5):
    n = int(input('Digite um número: '))
    if i == 0 or n > max(lista):
        lista.append(n)
        print('O valor foi adicionado ao final da fila.')
    else:
        for pos,valor in enumerate(lista):
            if n <valor:
                lista.insert(pos,n)
                print(f'Valor adicionado na posição {pos} valor {valor}')
                break
print(f'Valores na lista {lista}')
































