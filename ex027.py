#Faça um programa que leia o nome completo de uma pessoa.
#mostrando em seguida o primeiro e o ultimo nome separadamente.

# Solicita ao usuário que digite o nome completo e remove espaços extras
n = str(input('Digite seu nome completo: ')).strip()  # Recebe a entrada e remove os espaços extras no início e no fim

# Divide o nome completo em uma lista de palavras (separadas por espaços)
nome = n.split()  # O método .split() divide a string onde há espaços, criando uma lista com os nomes

# Exibe o primeiro nome, que é o primeiro elemento da lista
print('Seu primeiro nome é {}'.format(nome[0]))  # nome[0] acessa o primeiro elemento da lista, que é o primeiro nome

# Exibe o último nome, que é o último elemento da lista
print('Seu ultimo nome é {}'.format(nome[-1]))  # nome[-1] acessa o último elemento da lista, que é o último nome
