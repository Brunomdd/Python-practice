#Crie um programa que leia doisvlaores e mostre um menu ao lado da tela:
# seu programa deverá realizar a operação solicitada em cada caso.
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

from time import sleep
opr = 0
print("========Menu========")
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

while opr != 5:
    print("[ 1 ] Somar")
    print("[ 2 ] Multiplicar")
    print("[ 3 ] maior")
    print("[ 4 ] novos números")
    print("[ 5 ] sair do programa")
    opr = int(input("Digite uma das operações: "))
    sleep(2)

    if opr == 1:
     soma = n1+n2
     print(f'a soma entre {n1} + {n2} é igual a {soma}')
    elif opr == 2:
        mult = n1*n2
        print(f'a multiplicação entre {n1} x {n2} é igual a {mult}')
    elif opr == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"Entre {n1} e {n2} o maior valor é o {maior} ")
    elif opr == 4:
        print("Digite novos números: ")
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        print("números atualizados!")
    elif opr == 5:
        print("Finalizando. . .")
    else:
     print("Opção invalida tente novamente")










