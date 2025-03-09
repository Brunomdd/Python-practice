# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
# Inicializa a variável maior_peso com 0, para garantir que qualquer peso maior que 0 seja aceito como maior.
maior_peso = 0

# Inicializa a variável menor_peso com um valor muito alto (9999), para garantir que qualquer peso será considerado como menor no início.
menor_peso = 9999

# Loop que vai repetir 5 vezes para ler o peso de 5 pessoas.
for i in range(1, 6):
    # Lê o peso de cada pessoa e o converte para um número decimal (float).
    peso = float(input('Digite o peso da {} pessoa: '.format(i)))

    # Verifica se o peso atual é maior que o maior_peso registrado até agora.
    if peso > maior_peso:
        # Se for, o maior_peso é atualizado para o valor do peso atual.
        maior_peso = peso

    # Verifica se o peso atual é menor que o menor_peso registrado até agora.
    if peso < menor_peso:
        # Se for, o menor_peso é atualizado para o valor do peso atual.
        menor_peso = peso

# Ao final do loop, o programa imprime o maior e o menor peso registrados.
print("O maior peso foi de {}KG".format(maior_peso))
print("O menor peso foi de {}KG".format(menor_peso))
