numeros = []
while True:
    num = int(input("Digite um número: "))
    if num not in numeros:
        print('Valor adicionado com sucesso!')
        numeros.append(num)
    else:
        print('valor duplicado não vou adicionar')
    opr = ''
    while opr not in ['S','N']:
        opr = str(input("Quer continuar? [S/N]:")).strip().upper()
    if opr == 'N':
        break
print(f'os valores são {sorted(numeros)}')