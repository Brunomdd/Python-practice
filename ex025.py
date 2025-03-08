#Crie um programa que leia o nome de uma pessoa
#e pergunte se tem Silva no nome.
# Solicita ao usuário que informe o nome completo

nome = str(input('Qual é o Seu nome completo ?:')).strip()  # Recebe o nome completo e remove espaços extras antes e depois

# Verifica se o nome contém a palavra "Silva" (sem considerar maiúsculas ou minúsculas)
print('Seu nome tem Silva? {} '.format('Silva' in nome.upper()))  # Converte o nome para maiúsculo e verifica se "Silva" está presente
