# crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#depois disso, voce deve mostrar, para cada palavra, quais são as suas vogais.

palavras = (
    ("PROGRAMADOR"),
    ("CIENTISTA"),
    ("MOTORISTA"),
    ("PYTHON"),
    ("TRABALHAR"),
    ("MERCADO"),
    ("FUTURO"),
    ("GRATIS"),
)
vogais = 'aeiou'
for palavra in palavras:
    print(f'\nna Palavra {palavra} temos: ',end=' ')
    for i in range(len(palavra)):
        letra =  palavra[i]
        if letra.lower() in vogais:
            print(letra,end=' ')





















