#Crie um programa que calcule a idade de um atleta com base no ano de nascimento informado pelo usuário. Com a idade calculada,
# o programa deve classificar o atleta em uma categoria esportiva de acordo com a faixa etária:
#MIRIM: Até 9 anos.
#INFANTIL: De 10 a 14 anos.
#JUNIOR: De 15 a 19 anos.
#SENIOR: De 20 a 25 anos.
#MASTER: Acima de 25 anos.
from datetime import date

# Obtém o ano atual do sistema
ano_atual = date.today().year

# Solicita ao usuário o ano de nascimento do atleta
ano_nas = int(input("Digite seu ano de nascimento: "))

# Calcula a idade do atleta subtraindo o ano de nascimento do ano atual
idade = ano_atual - ano_nas

# Exibe a idade do atleta
print("O atleta tem {} anos. ".format(idade))

# Classifica o atleta em uma categoria de acordo com a idade:
# Se o atleta tem 9 anos ou menos, ele é classificado como MIRIM
if idade <= 9:
    print("MIRIM")
# Se o atleta tem entre 10 e 14 anos, ele é classificado como INFANTIL
elif idade <= 14:
    print("INFANTIL")
# Se o atleta tem entre 15 e 19 anos, ele é classificado como JUNIOR
elif idade <= 19:
    print("JUNIOR")
# Se o atleta tem entre 20 e 25 anos, ele é classificado como SENIOR
elif idade <= 25:
    print("SENIOR")
# Se o atleta tem mais de 25 anos, ele é classificado como MASTER
else:
    print("MASTER")