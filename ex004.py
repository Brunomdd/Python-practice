#Digite um programa que leia algo pelo teclado e mostre  na tela o seu tipo primitivo e
#todas as informações possíveis sobre ela.

# Solicita ao usuário que digite algo e armazena na variável 'a'
a = input(str('Digite algo:'))

# Verifica se a string contém apenas espaços em branco e imprime o resultado
print('Contém espaços?', a.isspace())
# 'isspace()' retorna True se a string contiver apenas espaços em branco, e False caso contrário.

# Verifica se a string é composta apenas por números e imprime o resultado
print('É numérico?', a.isnumeric())
# 'isnumeric()' retorna True se todos os caracteres na string forem números, e False caso contrário.

# Verifica se a string contém apenas letras maiúsculas e imprime o resultado
print('Tem letras maiúsculas?', a.isupper())
# 'isupper()' retorna True se todos os caracteres alfabéticos na string forem maiúsculos, e False caso contrário.

# Verifica se a string contém apenas letras minúsculas e imprime o resultado
print('Tem minúsculas?', a.islower())
# 'islower()' retorna True se todos os caracteres alfabéticos na string forem minúsculos, e False caso contrário.

# Verifica se a string contém apenas letras (sem números ou caracteres especiais) e imprime o resultado
print('É alfabético?', a.isalpha())
# 'isalpha()' retorna True se todos os caracteres na string forem letras (sem números ou espaços), e False caso contrário.

# Verifica se a string contém apenas caracteres alfanuméricos (letras e números) e imprime o resultado
print('É alfanumérico?', a.isalnum())
# 'isalnum()' retorna True se todos os caracteres na string forem letras ou números, e False caso contrário.

# Verifica se a string contém apenas caracteres decimais (números) e imprime o resultado
print('É decimal?', a.isdecimal())
# 'isdecimal()' retorna True se a string contiver apenas números decimais (e.g., '1234'), e False caso contrário.

# Verifica se a string está capitalizada (primeira letra maiúscula e as demais minúsculas) e imprime o resultado
print('Está capitalizado?', a.istitle())
# 'istitle()' retorna True se a string estiver no formato de título (prime
