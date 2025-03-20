# Lê um número inteiro fornecido pelo usuário para calcular o fatorial
num = int(input("Digite um número para calcular o fatorial : "))

# Inicializa a variável 'c' com o valor de 'num', que será usada para controlar a contagem no laço
c = num

# Inicializa a variável 'f' com 1, que será usada para armazenar o cálculo do fatorial
f = 1

# Enquanto 'c' for maior que 0, o loop continuará executando
while c > 0:
    # Exibe o número atual de 'c' na sequência de multiplicação do fatorial
    print("{}".format(c), end='')

    # Se 'c' for maior que 1, imprime "x", caso contrário, imprime "=" para indicar o fim da multiplicação
    print(f" x " if c > 1 else ' = ', end='')

    # Atualiza o valor de 'f' multiplicando-o pelo valor atual de 'c'
    f = f * c

    # Decrementa o valor de 'c' (subtrai 1)
    c += -1  # Ou seja, c = c - 1

# Após o loop, imprime o valor final do fatorial
print(f)
