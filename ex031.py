#Desenolva um programa que pergunte a distancia de uma viagem em km.
#calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200KM e R$0,45 para viagens
#mais longas

distancia = float(input('Qual a distancia da viagem?'))
if distancia <=200:
    preco = distancia *0.50
    print('Voce vai percorrer {} KMs e o preço da sua passagem será {}R$'.format(distancia,preco))
else:
    preco = distancia * 0.45
    print('o preço da sua passagem será de {}R$'.format(preco))



