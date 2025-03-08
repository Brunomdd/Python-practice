#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
#Pergunte o valor da casa, o salário do compador e em quantos anos vai pagar.
#A prestação mensal, não pode exceder 30% do salario
#ou então o empréstimo será negado.

# Solicita o valor da casa
casa = float(input('Valor da casa: R$:'))
# Solicita o salário do comprador
salario = float(input('Salário Comprador: R$'))
# Solicita o número de anos de financiamento
anos = int(input('Quantos anos de financiamento ?: '))
# Calcula a prestação mensal do financiamento (dividindo o valor da casa pelo número total de parcelas)
prestacao = casa / (anos * 12)
# Calcula o valor máximo que o comprador pode pagar por mês (30% do seu salário)
minimo = salario * 30 / 100
# Exibe o valor da casa, o número de anos e o valor da prestação mensal
print('Para pagar uma casa de R${:.2f} em {:.2f} anos'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f}'.format(prestacao))

# Verifica se o valor da prestação mensal é menor ou igual a 30% do salário
if prestacao <= minimo:
    # Se a prestação estiver dentro do limite, o empréstimo é aprovado
    print('\033[0;32;40mEmpréstimo Concedido!\033[m')
else:
    # Se a prestação ultrapassar o limite de 30% do salário, o empréstimo é negado
    print('EMPRÉSTIMO NEGADO')
