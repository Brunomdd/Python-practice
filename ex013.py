#Faça um algoritmo que leia o salário do funcionário e mostre o seu novo salário, com 15% de desconto.
salario = float(input('Digite o salário do funcionário R$'))
aumento = salario + (salario * 15 /100)
print('O funcionário que ganhava {}R$ terá um aumento de 15% e vai receber {}R$'.format(salario,aumento))