#Faca um programa que leia o nome e peso de várias pessoas,guardando tudo em uma lista.
# No final, mostre:

#A Quantas pessoas foram cadastradas.
#B Uma listagem com as pessoas mais pesadas.
#C Uma listagem com as pessoas mais leves.
temp = list()
princ = list()
maior = 0
menor = 0
cont = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = temp[1]
        menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    princ.append(temp[:])
    temp.clear()
    resp = ''
    while resp not in ['S','N']:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'Ao todo, voce cadastrou {len(princ)} pessoas')
print(f'O maior peso foi de {maior}Kg peso de ',end=' ')
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}]",end='')
print()
print(f'O menor peso foi de {menor}Kg peso de',end=' ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]',end='')
print()















