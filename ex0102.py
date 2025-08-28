#Refaça o exercicio 097: O programa deve fazer o seguinte:
#Armazenar os números pares e ímpares em listas separadas.
#Inserir cada número na respectiva lista de forma ordenada manualmente (ou seja, sem usar funções prontas como sorted()).
#Ao final, exibir as duas listas:
#A lista de números pares ordenada em ordem crescente.
#A lista de números ímpares ordenada em ordem crescente.
pares = list()
impares = list()
for i in range(0,8):
    n = int(input('Digite um número: '))
    if n % 2 ==0:
        if len(pares) == 0 or n > pares[-1]:
            pares.append(n)
        else:
            for pos,valor in enumerate(pares):
                if n <= valor:
                    pares.insert(pos,n)
                    break
    else:
        if len(impares) == 0 or n > impares[-1]:
            impares.append(n)
        else:
            for pos,valor in enumerate(impares):
                if n <= valor:
                    impares.insert(pos,n)
                    break
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')