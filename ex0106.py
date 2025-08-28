#Crie uma função em Python chamada tabuada que receba um número inteiro como parâmetro e exiba a tabuada desse número de 1 a 10.
def tabuada(n):
    for i in range(1,11):
        res = n*i
        print(f"{n} x {i} = {res}")
num = int(input('Digite um número: '))
tabuada(num)
