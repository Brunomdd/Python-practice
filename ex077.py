#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o avalor
# 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
#(Desconsiderando o flag).
n = 0
s = 0
cont= 0
while True:
    n = int(input("Digite um número: "))
    cont += 1
    if n == 999:
        break
    s += n
print(f"Foram digitados {cont} números e a A soma  entre eles foi {s}")


