lista = []
while True:
    palavras = input('Digite uma lista de palavras: ')
    lista.append(palavras)
    vazia = ''
    if palavras == vazia:
        break

letra= str(input('Digite uma letra: '))
cont = 0
for palavra in lista:
    if palavra != '':
        if palavra.lower()[0] == letra:
            cont +=1
     #if palavra.lower().startswith(letra):  # Ignora maiúsculas/minúsculas ou tem esse método também
# Passo 4: Mostrar o resultado
print(f'{cont} palavra(s) começam com a letra "{letra}".')


  
 