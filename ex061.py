#Crie um programa que leia  o ano de nascimento de sete pessoas.
#no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# Contadores para as pessoas maiores e menores de 18 anos

cont_mais18 = 0  # Variável para contar as pessoas maiores de 18 anos
cont_menos18 = 0  # Variável para contar as pessoas menores de 18 anos

# Importa o módulo date para pegar o ano atual
from datetime import date

# Obtém o ano atual usando o método today() do módulo date
atual = date.today().year  # O ano atual (ex: 2025)

# Inicia um laço (loop) que vai se repetir 7 vezes (uma para cada pessoa)
for i in range(1, 8):  # O loop será executado de 1 até 7 (totalizando 7 iterações)

    # Solicita ao usuário o ano de nascimento de cada pessoa (de 1ª a 7ª)
    ano = int(input('Digite o ano de nasc da {}ª pessoa: '.format(i)))

    # Calcula a idade da pessoa subtraindo o ano de nascimento do ano atual
    idade = atual - ano  # Exemplo: se o ano atual for 2025 e o ano de nascimento for 2003, a idade será 22.

    # Verifica se a pessoa tem 18 anos ou mais
    if idade >= 18:  # Se a idade for 18 ou mais, é maior de idade
        cont_mais18 += 1  # Se for maior de 18, incrementa o contador de pessoas maiores de idade
    else:  # Se a idade for menor que 18, a pessoa ainda é menor de idade
        cont_menos18 += 1  # Se for menor de 18, incrementa o contador de pessoas menores de idade

# Após o loop, imprime o resultado final, mostrando o total de pessoas maiores e menores de 18 anos
print("Ao todo tivemos {} pessoas maiores de idade.".format(cont_mais18))  # Exibe a quantidade de pessoas maiores de 18
print(
    'E também tivemos {} pessoas menores de idade'.format(cont_menos18))  # Exibe a quantidade de pessoas menores de 18


