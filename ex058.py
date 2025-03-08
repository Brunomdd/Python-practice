#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# Inicializa a variável 'cont' que irá contar quantos divisores o número tem
cont = 0

# Solicita ao usuário que insira um número inteiro e armazena esse valor em 'num'
num = int(input('Digite um número: '))

# Inicia um loop 'for' que vai de 1 até o número fornecido pelo usuário (inclusive)
for i in range(1, num + 1):
    # Verifica se o número 'num' é divisível por 'i' (ou seja, se o resto da divisão é zero)
    if num % i == 0:
        # Se for divisível, imprime o número em cor amarela (\033[33m)
        print('\033[33m', end='')
        # Aumenta o contador 'cont', indicando que o número foi divisível por 'i'
        cont += 1
    else:
        # Se não for divisível, imprime o número em cor roxa (\033[35m)
        print('\033[35m', end='')

    # Imprime o número 'i' sem pular linha e com a formatação aplicada acima
    print('{}'.format(i), end='')

# Exibe o total de divisores encontrados (valor de 'cont') para o número 'num'
print('\n\033[mO número {} foi divisível {} vezes'.format(num, cont))

# Se o número teve exatamente 2 divisores (1 e ele mesmo), ele é primo
if cont == 2:
    print('Ele é primo!')
else:
    print('Não é primo')
