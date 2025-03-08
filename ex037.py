#Escreva um programa que leia um número inteiro qualquer e peça
#para o usuário escolher qual será a base da conversão:
# 1 para Binário
# 2 para octal
#3 para hexadecimal

# Solicita ao usuário para digitar um número inteiro.
num = int(input('Digite um número:'))

# Exibe as opções para o usuário escolher o tipo de conversão que deseja fazer.
print('''Escolhe uma das bases para conversão:
[ 1 ] Para Binario
[ 2 ] Para Octal
[ 3 ] Para Hexadecimal ''')

# Solicita ao usuário para escolher uma das opções de conversão (1, 2 ou 3).
opcao = int(input('Sua opção:'))

# Verifica se a opção escolhida pelo usuário é 1 (binário).
if opcao == 1:
    # Converte o número para binário e remove o prefixo '0b', que é inserido automaticamente pelo Python.
    print('{} Convertido para Binário é igual a {}'.format(num,bin(num)[2:]))

# Verifica se a opção escolhida é 2 (octal).
elif opcao == 2:
    # Converte o número para octal e remove o prefixo '0o'.
    print('{} Convertido para Octal é igual a {}'.format(num,oct(num)[2:]))

# Verifica se a opção escolhida é 3 (hexadecimal).
elif opcao == 3:
    # Converte o número para hexadecimal e remove o prefixo '0x'.
    print('{} Convertido para Hexadecimal é igual a {}'.format(num,hex(num)[2:]))

# Se nenhuma das opções acima forem escolhidas, exibe uma mensagem de erro.
else:
    # Exibe a mensagem de erro em vermelho (com códigos de cor ANSI).
    print('\033[0;31;40mINCORRETO, Tente novamente!\033[m')
