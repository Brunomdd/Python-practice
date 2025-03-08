# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias

# Solicita ao usuário que insira a idade em anos, meses e dias
anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))

# Calcula a idade total em dias:
# 1. Multiplica o número de anos por 365 (aproximadamente o número de dias em um ano)
# 2. Multiplica o número de meses por 30 (aproximadamente o número de dias em um mês)
# 3. Adiciona os dias fornecidos pelo usuário
dias = dias + (anos * 365) + (meses * 30)

# Exibe a idade total em dias
print("A idade do usuário em dias é {}".format(dias))
