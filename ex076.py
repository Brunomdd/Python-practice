# Crie um programa que leia vários valores inteiros pelo teclado e no final da execução,mostre a média
# entre todos os valores lidos. O program deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = 0
cont = 0
resp = "S"
soma = 0
maior = 0
menor = 0
while resp =="S":
    num = int(input("Digite um número: "))
    soma +=num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
media = soma/cont
print("o usuário digitou {} números e a média entre eles foi {}".format(cont,media))
print("O maior número foi o  {} e o menor {}".format(maior,menor))






