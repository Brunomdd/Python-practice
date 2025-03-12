# Desenvolva um programa que leia o nome idade e sexo de 4 pessoas.
# no final do programa, mostre:
# a média de idade do grupo
# qual é o nome do homem mais velho.
#quantas mulheres tem menos de 20 anos.
# Inicializando variáveis para armazenar a soma das idades, média do grupo,
# nome e idade do homem mais velho, e contador de mulheres com menos de 20 anos.
soma_idade = 0
media_grupo = 0
maior_nome_h = ''
maior_idade_h = 0
cont_m = 0

# Estrutura de repetição para ler os dados de 4 pessoas
for i in range(1,5):
    print("======== {}ª Pessoa ========".format(i))  # Exibe o número da pessoa

    # Solicita o nome da pessoa
    nome = str(input("Digite o nome: "))

    # Solicita a idade e converte para inteiro
    idade = int(input("Digite a idade: "))

    # Solicita o sexo da pessoa (M para masculino, F para feminino)
    sexo = str(input("M/F: "))

    # Soma todas as idades para calcular a média posteriormente
    soma_idade += idade

    # Verifica se a pessoa é do sexo masculino e tem a maior idade registrada até o momento
    if sexo in 'Mm' and idade > maior_idade_h:
        maior_idade_h = idade  # Atualiza a maior idade encontrada
        maior_nome_h = nome  # Atualiza o nome do homem mais velho

    # Verifica se a pessoa é do sexo feminino e tem menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        cont_m = cont_m + 1  # Incrementa o contador de mulheres com menos de 20 anos

# Calcula a média de idade do grupo dividindo a soma total pelo número de pessoas
media_grupo = soma_idade / 4

# Exibe a média de idade do grupo
print("A média de idade do grupo é de {}".format(media_grupo))

# Exibe o nome e a idade do homem mais velho (caso haja homens no grupo)
print("O homem mais velho é o {} e ele tem {} anos".format(maior_nome_h, maior_idade_h))


# Exibe quantas mulheres têm menos de 20 anos
print("Existem {} mulheres com menos de 20 anos".format(cont_m))


