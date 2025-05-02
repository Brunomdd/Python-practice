#Crie um programa que leia vários números pelo teclado. O programa só vai parar
#quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre  (desconsiderando o flag)
num = 0
soma = 0
cont = 0
num = int(input("Digite o número: [999] para parar: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite o número: [999] para parar: "))
print("Foram digitados {} números e a soma total foi {}".format(cont,soma))
