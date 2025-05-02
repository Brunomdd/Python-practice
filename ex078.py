#Faça um programa que mostre a tabuada e vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número soliticado for negativo ou zero.
print("\nTABUADA COM FLAG")
print("--"*10)
while True:
    cont =0
    num = int(input("Quer ver a tabuada de qual valor ?: "))
    if num <0 or num == 0:
        break
    while cont <10:
        cont = cont+1
        res = num * cont
        print(f" {num} x {cont} = {res}")
print("Fim de programa")




