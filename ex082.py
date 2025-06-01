#Crie um programa que simule o funcionamento de um caixa eletronico. No início,pergunte ao usuário qual será o valor
#a ser sacado ( número inteiro) e o programa vai informar quantas células de cada valor serão entregues
#Considere que o caixa tem cédulas de# R$50# R$20 # R$10 e #R$1

print('='*20)
print('{:^15}'.format('CAIXA ELETRONICO'))
print('='*20)


print('='*20)
print('{:^15}'.format('CAIXA ELETRONICO'))
print('='*20)

# Recebe o valor que o usuário quer sacar
valor = int(input("Informe o Valor R$: "))

# 'total' começa com o valor do saque, vai diminuindo ao longo do processo
total = valor

# Começamos pelas cédulas de 50 reais
céd = 50

# Contador para saber quantas cédulas daquela estão sendo usadas
total_céd = 0

# Loop infinito que só vai parar quando o saque for concluído
while True:
    # Se ainda dá pra tirar uma cédula desse valor
    if total >= céd:
        total -= céd         # Tira o valor da cédula do total
        total_céd += 1       # Conta uma cédula usada
    else:
        # Se usamos pelo menos uma cédula desse valor, mostramos na tela
        if total_céd > 0:
            print(f'No total {total_céd} notas de R${céd} foram imprimidas')

        # Agora trocamos pra próxima cédula menor
        if céd == 50:
            céd = 20

        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1

        # Resetamos o contador pra nova cédula
        print(f"[DEBUG] Troca para cédula de R${céd} e zera contador")

        total_céd = 0

        # Se já tiramos todo o dinheiro, encerramos o loop
        if total == 0:
            break






