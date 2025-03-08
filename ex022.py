#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras Maiúsculas e minúsculas.
#Quantas letras tem ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome
# Pede para o usuário digitar o nome completo e remove quaisquer espaços extras nas extremidades da string com .strip().
nome = input(str('Informe o seu nome completo: ')).strip()

# Exibe uma mensagem indicando que o nome será analisado.
print('Analisando seu nome...')

# Exibe o nome completo em maiúsculas, usando o método .upper() que converte todos os caracteres para maiúsculos.
print('Seu nome em maiúsculo é {}'.format(nome.upper()))

# Exibe o nome completo em minúsculas, usando o método .lower() que converte todos os caracteres para minúsculos.
print('Em minúsculo {}'.format(nome.lower()))

# Essa linha está comentada. Ela mostraria o número total de letras no nome, excluindo espaços.
# A expressão `len(nome)` conta todos os caracteres, e `nome.count(' ')` conta quantos espaços existem.
# Subtrair o número de espaços de `len(nome)` daria o número de letras. Porém, foi comentada no código.
# Aqui, o método .find() retorna o índice do primeiro espaço (' '). Isso não retorna o número de letras no primeiro nome,
# mas sim a posição em que ocorre o primeiro espaço. Por exemplo, para "Ana Maria", o método .find(' ') retorna 3,
# pois o espaço aparece na posição 3 (considerando a indexação que começa do zero).
# Isso não serve para contar as letras do primeiro nome, mas é a posição onde o primeiro nome termina.
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))  ## Isso não está correto para contar as letras do primeiro nome.

# O método .split() divide a string "nome" em uma lista de palavras, separadas por espaços.
# Por exemplo, se o nome for "Ana Maria", a lista resultante será ['Ana', 'Maria'].
separa = nome.split()

# Exibe o primeiro nome (separa[0]) e o número de letras desse primeiro nome.
# O primeiro nome é a primeira palavra da lista criada pelo .split().
# O len(separa[0]) retorna o número de letras do primeiro nome.
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

