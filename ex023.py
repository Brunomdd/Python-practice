#Faça um programa em Python que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Pede para o usuário informar um número inteiro e o converte para tipo int
num = int(input('Informe um número: '))

# Calcula a unidade (último dígito do número)
# O operador // faz divisão inteira, então 'num // 1' basicamente retorna o número inteiro,
# e % 10 vai pegar o último dígito (unidade) do número.
unidade = num // 1 % 10

# Calcula a dezena (penúltimo dígito do número)
# 'num // 10' remove a unidade (último dígito) do número, e depois o % 100 pega os dois últimos dígitos (dezena e unidade).
# Isso resulta apenas na dezena se o número tiver pelo menos dois dígitos.
dezena = num // 10 % 100

# Calcula a centena (terceiro dígito do número)
# 'num // 100' remove as duas últimas casas (unidade e dezena), e depois o % 10 pega o terceiro dígito (centena).
centena = num // 100 % 10

# Calcula o milhar (quarto dígito do número)
# 'num // 1000' remove as três últimas casas (unidade, dezena e centena), e depois o % 10 pega o quarto dígito (milhar).
milhar = num // 1000 % 10

# Exibe o valor de cada uma das casas (unidade, dezena, centena, milhar)
print('Unidade  {}'.format(unidade))  # Exibe o valor da unidade
print('Dezena {}'.format(dezena))    # Exibe o valor da dezena
print('Centena é {}'.format(centena)) # Exibe o valor da centena
print('Milhar {}'.format(milhar))    # Exibe o valor do milhar
