#Crie um programa em que:
#Tenha uma tupla chamada dias contendo os dias da semana, começando por "Domingo" até "Sábado".
#Peça ao usuário que digite um número de 0 a 6.
#Mostre na tela o dia da semana correspondente ao número digitado, usando a tupla.
#Se o número estiver fora do intervalo de 0 a 6, exiba uma mensagem de erro: "Número inválido."
dias = ('Domingo','Segunda-Feira','Terça-Feira','Quarta-Feira','Quinta-Feira','Sexta-Feira','Sábado')
numero = int(input("Digite um número entre 0 e 6: "))
if 0 <= numero <=7:
    print(f"O dia correspondente é {dias[numero-1]}")
else:
    print("Dia inválido")