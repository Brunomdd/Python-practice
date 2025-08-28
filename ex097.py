#Crie um programa onde o usuário digite uma expressão qualquer que use parenteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.
cont = 0
exp = input('Digite uma expressão')
for símb in exp:
    if símb == '(':
        cont +=1
    elif símb == ')':
        cont -=1
    if cont <0:
        print('Expressão inválida:')
        break

else:
    if cont == 0:
        print('Expressão válida')
    else:
        print('Expressão inválida')







