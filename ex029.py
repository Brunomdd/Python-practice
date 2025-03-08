#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 Km/H. mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar 7,00 por cada Km acima do Limite.

# Solicita ao usuário que digite a velocidade do condutor e converte para um número de ponto flutuante
velocidade = float(input('Digite a velocidade do condutor: '))

# Verifica se a velocidade informada é maior que 80 km/h
if velocidade > 80:
    # Se a velocidade for superior a 80 km/h, calcula a multa. A multa é de R$7,00 por km/h acima do limite de 80 km/h.
    multa = (velocidade - 80) * 7

# Exibe o valor da multa caso o condutor tenha excedido a velocidade
print('MULTADO POR EXCESSO DE Velocidade. Você pagará uma multa de {}R$'.format(multa))

