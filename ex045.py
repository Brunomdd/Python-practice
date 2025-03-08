# O programa deve ler dois números inteiros e comparar os valores.
# Ele irá verificar qual dos números é maior, ou se ambos são iguais.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

# Comparando os números
if n1 > n2:
    print("O primeiro valor é maior!!")
elif n2 > n1:
    print("O segundo valor é maior!!")
else:
    print("Os dois valores são iguais!!")
