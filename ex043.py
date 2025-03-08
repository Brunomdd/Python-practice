# Desenvolva um programa usando a estrutura “para” que mostre na tela a
#seguinte contagem:
#0 5 10 15 20 25 30 35 40 Acabou!

# Inicia o loop 'for' com a variável 'i' que vai percorrer os valores de 0 até 40
# A função range(0, 41) vai gerar números de 0 até 40 (41 não é incluído)
for i in range(0, 41):
    # Imprime o valor de 'i' a cada iteração do loop
    print("{}".format(i))

# Após o término do loop, imprime a mensagem "Acabou!".
# Esse print vai ser executado apenas uma vez, após todos os números terminar.
