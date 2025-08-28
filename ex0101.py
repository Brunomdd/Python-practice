#Aprimore o desafio anterior, mostrando no final:
#A A soma de todos os valores pares digitados
#B A soma dos valores da terceira coluna.
#C O maior valor da segunda linha
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = 0
coluna = 0
maior = 0
l = 0
while l < 3:
    c = 0
    while c < 3:
        matriz[l][c] = int(input(f'Digite um valor nas poisições {l} {c}: '))
        c += 1
    l +=1
l = 0
while l < 3:
    c = 0
    while c < 3:
        print(f"[{matriz[l][c]:^5}]",end=' ')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        c+=1
    print()
    l+=1
print(f"A quantidade de números pares é {spar}")
for l in range(0,3):
    coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {coluna}')
for c in range(0,3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é  o {maior}")
