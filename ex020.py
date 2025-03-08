# O mesmo professor do desafio anterior quer sortear a ordem de apresentacão dos alunos.
# Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.


# Importa a função 'shuffle' do módulo 'random', que será usada para embaralhar a lista.
from random import shuffle

# Solicita ao usuário o nome do primeiro aluno e armazena na variável 'n1'.
n1 = str(input('Nome do primeiro aluno: '))

# Solicita ao usuário o nome do segundo aluno e armazena na variável 'n2'.
n2 = str(input('Nome do segundo aluno: '))

# Solicita ao usuário o nome do terceiro aluno e armazena na variável 'n3'.
n3 = str(input('Nome do terceiro aluno: '))

# Solicita ao usuário o nome do quarto aluno e armazena na variável 'n4'.
n4 = str(input('Nome do quarto aluno: '))

# Cria uma lista chamada 'lista' contendo os nomes dos quatro alunos.
lista = [n1, n2, n3, n4]

# Usa a função 'shuffle' para embaralhar aleatoriamente a ordem dos elementos da lista 'lista'.
# Note que 'shuffle' não retorna um valor, ele modifica a lista original diretamente.
sorteio = shuffle(lista)

# A função shuffle() não retorna um valor, então a variável 'sorteio' será 'None'.
# Aqui, estamos imprimindo o conteúdo da lista já embaralhada.
# A impressão da lista já está sendo feita diretamente.
print('O escolhido foi {}'.format(lista))
