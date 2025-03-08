# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo
# do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

# Obtém o ano atual do sistema
atual = date.today().year

# Solicita ao usuário o ano de nascimento
ano_nas = int(input("Digite o ano de nascimento: "))

# Solicita ao usuário o ano atual
ano_atual = int(input("Digite o ano atual: "))

# Calcula a idade da pessoa
idade = ano_atual - ano_nas

# Exibe a idade da pessoa
print("Quem nasceu em {} tem {} anos em {}".format(ano_nas, idade, ano_atual))

# Verifica se a pessoa tem exatamente 18 anos (ano de alistamento)
if idade == 18:
    print("Você precisa ir se alistar imediatamente!!")

# Se a pessoa tem menos de 18 anos, calcula o tempo restante para o alistamento
elif idade < 18:
    saldo = 18 - idade  # Quantos anos faltam para a pessoa completar 18 anos
    print("Ainda faltam {} anos para o alistamento".format(saldo))

    # Calcula o ano em que a pessoa terá 18 anos e se alistará
    ano = atual + saldo
    print("Seu alistamento será em {}".format(ano))

# Se a pessoa tem mais de 18 anos, calcula quantos anos se passaram após o alistamento
elif idade > 18:
    saldo = idade - 18  # Quantos anos se passaram desde o alistamento
    print("Já se passaram {} anos do seu alistamento".format(saldo))

    # Calcula o ano em que a pessoa se alistou
    ano = atual - saldo
    print("Seu alistamento foi em {}".format(ano))

