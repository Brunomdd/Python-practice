numero = []
while True:
    numero.append((int(input('Digite um numero: '))))
    resp = str(input('Quer continuar?[ Digite N para parar o programa]: ')).strip().upper()
    if resp in 'Nn':
        break
print(f'Foram digitados {len(numero)} números.')
numero.sort(reverse=True)
print(f'A lista na ordem decrescente é {numero}')
if 5 in numero:
    print('O número 5 esta na lista!')
else:
    print('O número 5 não está na lista')
