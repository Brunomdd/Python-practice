#Crie um algoritmo que leia um número inteiro e mostre seu  dobro,triplo e raiz quadrada.
# Solicita ao usuário que digite um número e converte para inteiro
num = int(input('Digite um número:'))

# Calcula o dobro do número
dob = num * 2

# Calcula o triplo do número
trip = num * 3

# Calcula a raiz quadrada do número
raiz = num ** (1 / 2)

# Exibe os resultados: o dobro, o triplo e a raiz quadrada, formatando o resultado da raiz para 2 casas decimais
print('O dobro do número é igual a {}. O triplo do número é {} e a raiz é {:.2f}'.format(dob, trip, raiz))
# A função 'format()
