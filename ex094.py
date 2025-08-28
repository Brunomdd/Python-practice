numeros = []
par = []
impar = []
while True:
    num = int(input("Digite um valor: "))
    numeros.append(num)
    if num % 2 == 0:
        par.append(num)
    if num % 2 == 1:
        impar.append(num)
    resp = ''
    while resp not in ['S','N']:
        resp = str(input("Quer continuar? [S/N]: ")).upper().strip()
    if resp == 'N':
        break
print(f'A lista completa é {numeros}')
print(f'A lista com numeros pares é {par}')
print(f'A lista com numeros impares é {impar}')

