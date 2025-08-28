#Crie um programa em Python que leia uma palavra digitada pelo usuário e realize as seguintes tarefas:
#Conte quantas vogais existem na palavra.
#Identifique quais vogais aparecem na palavra, sem repetições.
#Exiba o total de vogais encontradas e a lista das vogais distintas presentes na palavra.
#Regras:
#Considere apenas as vogais: a, e, i, o, u (maiúsculas ou minúsculas devem ser tratadas igualmente).
#A lista de vogais encontradas deve ser exibida em letras minúsculas e na ordem em que apareceram pela primeira vez na palavra.
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


