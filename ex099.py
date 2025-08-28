#Crie um programa que o usuário possa digitar sete valores Númericos e cadastre-os numa
# lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares e
# impares em ordem crescente.
valores = list()
pares = list()
impares = list()

for i in range(0,7):
    num  = int(input(f'Digite  o {i} valor: '))
    if num % 2 == 0:
        pares.append(num)
    if num % 2 ==1:
        impares.append(num)
valores = [pares,impares]

print(f'Os valores pares digitados foram {sorted(valores[0])}')
print(f'Os valores impares digitados foram {sorted(valores[1])}')










