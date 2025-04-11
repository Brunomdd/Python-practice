#Exercício: Tabuada
#Crie um programa que, a partir de um número que o usuário digitar, mostre a tabuada desse número de 1 a 10. usando o while

n = int(input("Digite um número para a tabuada: "))
c = 1
while c <=10:
    res = n * c
    print("{} x {} = {} ".format(n,c,res))
    c += 1
