# Algoritmo para ler o peso e altura de 7 pessoas e fornecer algumas estatísticas sobre o grupo.
# O programa realiza as seguintes tarefas:
# a) Calcula a média de altura do grupo.
# b) Conta quantas pessoas pesam mais de 90kg.
# c) Conta quantas pessoas pesam menos de 50kg e têm altura menor que 1.60m.
# d) Conta quantas pessoas têm mais de 1.90m de altura e pesam mais de 100kg.

# Inicializando as variáveis
cont = 1  # Contador para 7 pessoas
soma_altura = 0  # Para somar as alturas
peso_mais90 = 0  # Contador de pessoas com peso acima de 90kg
peso_menor50 = 0  # Contador de pessoas com peso abaixo de 50kg e altura menor que 1.60m
altura_mais190 = 0  # Contador de pessoas com altura maior que 1.90m e peso maior que 100kg

# loop para ler os dados de 7 pessoas

while cont <= 7:
    # Solicitar o peso e a altura para cada pessoa
    print("=============================")
    print("Digite o {}º peso e altura da pessoa".format(cont))
    print("=============================")

    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    # Acumulando as alturas para o cálculo da média
    soma_altura = soma_altura + altura

    # Contando as pessoas com peso maior ou igual a 90kg
    if peso >= 90:
        peso_mais90 = peso_mais90 + 1
    # Contando as pessoas que pesam menos de 50kg e têm menos de 1.60m de altura
    if peso < 50 and altura < 1.60:
        peso_menor50 = peso_menor50 + 1

    # Contando as pessoas que têm mais de 1.90m de altura e pesam mais de 100kg
    if altura > 1.90 and peso >= 100:
        altura_mais190 = altura_mais190 + 1

    # Incrementa o contador para a próxima pessoa
    cont = cont + 1

# Calculando a média das alturas
media = soma_altura / 7
print("A média de altura do grupo foi {:.2f}".format(media))
print("Pessoas com mais de 90KG {}".format(peso_mais90))
print("pessoas que pesam menos de 50Kg e tem menos de 1.60m {}".format(peso_menor50))
print("pessoas que medem mais de 1.90m  e pesam mais de 100Kg {}".format(altura_mais190))




