numeros = []
for c in range(0,5):
    numeros.append(int(input(f"Digite um número na posição {c}: ")))
print(f'O maior número digitado foi {max(numeros)} na posição',end=' ')
for pos,valor in enumerate(numeros):
    if valor == max(numeros):
        print(f'{pos}',end='')
print()
print(f'O menor valor digitado foi {min(numeros)} na posição',end=' ')
for pos,valor in enumerate(numeros):
    if valor == min(numeros):
        print(f"{pos}",end='')
print()

