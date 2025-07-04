vogais_encontradas = ''
cont = 0
vogais = 'aeiou'
palavra = str(input("Digite uma palavra: "))
for i in range(len(palavra)):
    letra = palavra[i]
    if letra.lower() in vogais:
        cont +=1
        if letra.lower() not in vogais_encontradas:
             vogais_encontradas += letra.lower()
print(f"A palavra {palavra} tem {cont} vogais")
print(f"Vogais encontradas: {vogais_encontradas}")


