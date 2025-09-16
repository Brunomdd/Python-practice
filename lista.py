lista = []
while True:
    produto = input('Nome do produto: ')
    lista.append(produto)
    resp = str(input('Quer continuar? [S/N]:')).strip().upper()
    if resp == 'N':
        break
for pos, valor in enumerate(lista):
    print(f'Item {pos}: {valor}')

while True:
    remover = str(input('Quer remover algum item? [S/N]: ')).strip().upper()
    if remover == 'S':
        numero = int(input('Digite o numero do item que quer remover: '))
        if numero >=0 and numero <= len(lista):
            lista.pop(numero)
        else:
            print('Inválido')
        break
print('Lista final: ')
for pos, valor in enumerate(lista):
    print(f'Item {pos}: {valor}')

