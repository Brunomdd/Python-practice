#Refaça o exercício 60 usando o while: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços usando o while.

# Solicita ao usuário que digite uma frase, converte para maiúsculas e remove espaços extras nas pontas
frase = str(input("Digite uma frase: ")).upper().strip()

# Separa a frase em palavras, criando uma lista
palavras = frase.split()

# Junta todas as palavras sem espaços
junto = ''.join(palavras)

# Define a variável 'letra' como o índice do último caractere da string 'junto'
letra = len(junto) - 1

# Cria uma variável vazia para armazenar o texto invertido
inverso = ''

# Enquanto o índice 'letra' for maior ou igual a 0, pega os caracteres de trás para frente
while letra >= 0:
    inverso = inverso + junto[letra]  # Adiciona o caractere atual ao inverso
    letra -= 1  # Decrementa o índice para ir para o caractere anterior

# Mostra o texto original e o seu inverso
print(f"O inverso de {frase} é  {inverso}")

# Verifica se o texto invertido é igual ao texto original (sem espaços e em maiúsculas)
if inverso == junto:
    print("temos um palíndromo")  # Se forem iguais, é um palíndromo
else:
    print("não é um palíndromo")  # Se forem diferentes, não é um palíndromo

