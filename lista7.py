lista =[]
c = 0
s =0
#1
while c < 5:
    usuario = int(input('Digite um número: '))
    s += usuario
    lista.append(usuario)
    c +=1
#2
maior = lista[0]
menor = lista[0]
for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
#3
print(f'O maior número da lista é o {maior}')
print(f'O menor número da lista é o {menor}')
#4
media = s/len(lista)
print(f'A soma dos números é {s} e a média é {media:.2f}' )
#5
usuario = int(input('Digite um número para ver se ele exista na lista: '))
if usuario in lista:
    print(f'O número {usuario} está na lista')

#6
outra_lista =[]
for num in lista:
    outra_lista.append(num*2)
print(outra_lista)
 

