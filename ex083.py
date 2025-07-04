#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado entre (0 e 20) e mostra-lo por extenso.
extenso = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'quatorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <=20:
        print(f'Voce digitou o número {extenso[numero]} ')
    else:
        print('tente novamente')
    resp = ''
    while resp != 'S'and resp != 'N':
        resp = input('Quer continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break
print('Fim de programa')
