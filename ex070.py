#Crie um programa que peça ao usuário para digitar números inteiros.
# O programa deve continuar pedindo números até que o usuário digite o número 0.
# Quando o número 0 for digitado, o programa deve mostrar a soma de todos os números digitados, exceto o 0.
soma = 0

num = int(input("Digite um número inteiro: "))
while num != 0:
    soma += num
    num = int(input("Digite um número inteiro: "))
print(f"a soma de todos os números é: {soma}")

