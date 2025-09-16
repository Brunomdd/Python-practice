#exercicio — Lista de produtos simples
#Faça um programa que:
#Receba o nome de 5 produtos do usuário (um por vez)
#Armazene esses nomes em uma lista
#No final, mostre todos os produtos digitados, enumerados (com índice)
#Exercício 2 — Remover produto por índice
#Agora, usando a lista do exercício 1:
#Pergunte ao usuário se ele quer remover algum produto (S/N)
#Se sim, peça o índice do produto a ser removido
#Remova o produto da lista (verificando se o índice é válido)
#Mostre a lista atualizada

lista = []
for i in range(5):
    produto = str(input('Digite o nome do produto: '))
    lista.append(produto)

print('Lista:')
for pos,valor in enumerate(lista):
    print(f'{pos} {valor}')

while True:
    remover = str(input('Quer remover algum produto: ?')).strip().upper()
    if remover == 'S':
        numero = int(input('Quer remover qual produto?:'))
        if 0 <= numero < len(lista):
            removido = lista.pop(numero)
            print(f'Produto {removido} removido com sucesso!')
    elif remover == 'N':
        break
    else:
        print('Resposta inválida digite [S/N]')

print('Lista atualizada: ')      
for pos,valor in enumerate(lista):
    print(f'{pos} {valor}')




    
   
