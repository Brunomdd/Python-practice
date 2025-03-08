#Faça  um algoritmo que leia um preço de um produto e seu novo preço com 5 % de desconto.
produto = float(input('Digite o preço do produto R$'))
desconto = produto - (produto * 5/100)
print('O produto custava {}R$ com o desconto, o produto ficará {}R$'.format(produto,desconto))
