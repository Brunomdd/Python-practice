# Crie um programa que leia a idade e o sexo de várias pessas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# no final mostre:
# A quantas pessoas tem mais de 18 anos.
#B Quantos homens foram cadastrados
#C Quantas mulheres tem, menos de 20 anos
from time import sleep
cont_18 =0
cont_h = 0
cont_m = 0
print('\033[36m*='*20)
print("\tANALISE DE DADOS DO GRUPO")
print('*='*20)
while True:
    idade = int(input("Digite a idade: "))
    sexo = ' '
    while sexo != 'M' and sexo !='F':
        sexo = str(input("Digite o sexo [M/F]: ")).upper().strip()
        if sexo != 'M' and sexo != 'F':
            print("\033[31m Incorreto Tente novamente")
        else:
            print("\033[31mREGISTRANDO USUÁRIO . . .\033[m")
        sleep(2)
    if idade >=18:
        cont_18 +=1
    if sexo =='M':
         cont_h +=1
    if sexo == 'F' and idade <20:
        cont_m +=1
    resp = ' '
    while resp != 'S' and resp != 'N':
         resp = str(input("\033[34mQuer continuar com o cadastro [S/N]?: ")).strip().upper()
    if resp == 'N':  # Se o usuário digitar 'N', o loop principal para
        break
print("\n\033[36m========= RESULTADO FINAL =========\033[m")
print(f"\033[33mForam cadastradas {cont_18} pessoas com mais de 18 anos.\033[m")
print(f"\033[34mForam cadastrados {cont_h} homens.\033[m")
print(f"\033[35mE temos {cont_m} mulheres cadastradas com menos de 20 anos.\033[m")
print("\033[36m===================================\033[m")




