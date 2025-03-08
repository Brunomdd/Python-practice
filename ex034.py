#Escreva um programa qaue pergunte o salárioo de um funcionário e
#calcule o valor do seu aumento.
#PAra Salários superiores a R$1.250,00,calcule um aumento de 10%
#para salarios inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o salário do funcionario:'))
if salario <=1250:
    aumento = salario + (salario*15/100)
else:
    aumento = salario +(salario*10/100)
print('Quem ganhava \033[1:30:97m{:.2f}R$ passa a ganhar \033[5;97;42m{}$\033[m'.format(salario,aumento))