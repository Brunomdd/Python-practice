# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10 % de desconto
# a vista no cartao: 5% de desconto
# em até 2X no cartao: preço normal
# 3X ou mais no cartao; 20% de juros

# Solicita ao usuário o preço das compras e armazena em uma variável chamada 'preço'
preço = float(input("Preço das compras R$:"))

# Exibe as opções de pagamento para o usuário
print("[1] À vista Dinheiro/Cheque")
print("[2] À vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x no cartão ou mais")

# Solicita ao usuário escolher uma das opções de pagamento e armazena a escolha em 'opr'
opr = int(input("Escolha a opção: "))

# Condição para o pagamento à vista, seja em dinheiro ou cheque (opção 1)
if opr == 1:
    # Aplica um desconto de 10% no preço para o pagamento à vista
    total = preço - (preço * 10 / 100)
# Condição para o pagamento à vista no cartão (opção 2)
elif opr == 2:
    # Aplica um desconto de 5% no preço para o pagamento à vista no cartão
    total = preço - (preço * 5 / 100)
# Condição para parcelamento em 2x no cartão (opção 3)
elif opr == 3:
    # Para o parcelamento em 2x, o preço é o mesmo (sem descontos ou juros)
    total = preço
    # Calcula o valor de cada parcela, dividindo o total por 2
    parcela = total / 2
    # Exibe a informação sobre o parcelamento em 2x
    print("Sua compra será parcelada em 2x de R${:.2f}".format(parcela))
# Condição para parcelamento em 3x ou mais no cartão (opção 4)
elif opr == 4:
    # Aplica 20% de juros no preço para o parcelamento acima de 2x
    total = preço + (preço * 20 / 100)
    # Solicita ao usuário o número de parcelas para o parcelamento em 3x ou mais
    totparcelas = int(input("Quantas parcelas?: "))
    # Calcula o valor de cada parcela dividindo o total (com juros) pelo número de parcelas
    parcela = total / totparcelas
    # Exibe a informação sobre o parcelamento com juros
    print("Sua compra será parcelada em {}x de R${:.2f} COM juros".format(totparcelas, parcela))
# Exibe o valor final da compra, com o preço original e o total a ser pago
else:
    total = 0
    print("\033[1:30:97m Opção errada de pagamento, tente novamente!\033[m;")
print("\033[3:32:33mSua compra de R${:.2f} vai acabar custando R${:.2f} no final \033[m".format(preço, total))
