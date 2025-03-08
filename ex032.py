#faça um programa que leia um ano qualquer e diga se ele é bissexto.
from datetime import date

# Solicita ao usuário que informe um ano para ser analisado
ano = int(input('Em que Ano quero Analisar ?:'))

# Verifica se o ano é bissexto
# Um ano é bissexto se:
# - for divisível por 4, mas não divisível por 100, ou
# - for divisível por 400
if ano %4 == 0 and ano %100 != 0 or ano %400 == 0:
    # Se a condição for verdadeira, imprime que o ano é bissexto
    print('O {} é bissexto'.format(ano))
else:
    # Caso contrário, imprime que o ano não é bissexto
    print('O ano {} não é bissexto'.format(ano))