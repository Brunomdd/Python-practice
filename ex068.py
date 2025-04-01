# Crie um programa que faça uma contagem regressiva a partir de um número que o usuário digitar.
#O programa deve exibir os números um a um, até chegar a 0.
# Quando chegar a 0, deve imprimir " Feliz Ano Novo!" e encerrar o programa.

from time import sleep

num = int(input("Digite um número para inicar a contagem: "))
c = num
while  c >=0 :
    print(c,end='  ')
    c -= 1
    sleep(0.5)
print("\nFeliz ano novo!")
