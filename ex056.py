soma = 0  # Inicializa a variável 'soma' com 0, que será usada para armazenar a soma dos números pares

# Laço de repetição que vai de 1 até 6 (6 iterações, porque o range vai até 7)
for i in range(1, 7):
    # Pede ao usuário para digitar um número, e mostra qual número ele está digitando (1º, 2º, etc.)
    num = int(input('Digite o {} número: '.format(i)))
    # Verifica se o número digitado é par (se o resto da divisão por 2 for igual a 0)
    if num % 2 == 0:
        # Se o número for par, ele é somado à variável 'soma'
        soma = soma + num

# Após o loop, exibe a soma de todos os números pares digitados
print('A soma de todos os pares é {}'.format(soma))
