#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
#lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = 0
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
            spar += matriz
        c+=1
    print()
    l+=1


