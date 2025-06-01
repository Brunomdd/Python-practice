#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final mostre:
#A) Qual é o  total gasto na compra
#B) Quantos produtos custam mais de 1000R$
#C) qual é o nome do produto mais barato
total = 0
cont_produtos = 0
cont = 0
menor = 0
produto_menor = ''
resp = ' '
print("=*"*20)
print("\tESTATÍSTICA EM PRODUTOS")
print("=*"*20)
while True:
    nome_produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto R$: "))
    total += preco
    cont +=1
    if preco > 1000:
        cont_produtos +=1

    if cont == 1:
        menor = preco
        produto_menor = nome_produto
    else:
        if preco < menor:
            menor = preco
            produto_menor = nome_produto
    resp = ' '
    while resp != 'S' and resp != 'N':
        resp = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
    if resp == 'N':
        break
print(f"O total da compra é de {total} R$")
print(f"No total tem {cont_produtos} valores maiores que 1000 R$")
print("O produto mais barato custa {:.2f} e o nome é {}".format(menor,produto_menor))
