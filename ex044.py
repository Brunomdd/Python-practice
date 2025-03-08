#Faça um programa usando a estrutura “para” que leia um número inteiro
#positivo e mostre na tela uma contagem de 0 até o valor digitado:
#Ex: Digite um valor: 9
#Contagem: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, FIM!

# Solicita ao usuário que digite um número
num = int(input("Digite um número: "))  # A entrada do usuário é convertida para um número inteiro e armazenada em 'num'

# Exibe a mensagem "Contagem:" antes de começar a contagem
print("Contagem: ",end="")

# Loop 'for' que vai de 0 até o número digitado (inclusive)
# O range(num + 1) vai gerar números de 0 até 'num', incluindo o próprio 'num'
for i in range(num + 1):
    # Imprime o valor de 'i' na mesma linha, separado por espaço
    print(i, end=' ')  # O 'end=" "' garante que os números fiquem na mesma linha, separados por espaços

# Após o loop, imprime a mensagem "FIM!!" para indicar o fim da contagem
print("FIM!!")  # Essa linha é executada depois que o loop termina, indicando o fim da cont

