# Solicita ao usuário que digite uma frase, remove espaços extras no começo e no final,
# e transforma a frase para letras maiúsculas.
frase = str(input('Digite a frase: ')).strip().upper()

# Divide a frase em palavras separadas por espaços.
palavras = frase.split()

# Junta as palavras de volta em uma única string, sem espaços.
junto = ''.join(palavras)

# Inicializa a variável 'inverso' que vai armazenar o inverso da string 'junto'
inverso = ''

# Método 2 para gerar o inverso da string usando slicing.
# 'junto[::-1]' é uma forma compacta de reverter a string, pegando todos os caracteres de trás para frente.
inverso = junto[::-1]

# Método 1 (comentado) usaria um loop 'for' para reverter a string manualmente.
# No caso, o código não está utilizando esse método, mas ele funcionaria da seguinte maneira:
# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]

# Exibe a string original sem espaços e a sua versão invertida.
print("O inverso de {} é  {}".format(junto, inverso))

# Compara se a string original (junto) é igual à sua versão invertida (inverso).
# Se forem iguais, significa que a frase é um palíndromo.
if inverso == junto:
    print("Temos um palíndromo!")  # Exibe mensagem informando que a frase é um palíndromo
else:
    print('A frase digitada não é um palíndromo!')  # Exibe mensagem dizendo que não é um palíndromo
