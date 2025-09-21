def mostrarlista():
     for pos,valor in enumerate(lista,1):
        print(f'{pos}: {valor}')

lista = []
while True:
    produtos = str(input('Digite os produtos: '))
    lista.append(produtos)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    mostrarlista()
        
    if resp in 'Nn':
        break
    
while True: 
    remover = str(input('Quer remover algum produto?')).strip().upper()
    if remover == 'S':
        mostrarlista()
        item_removido = str(input('Digite o item a ser removido: '))
        if item_removido in lista:
            lista.remove(item_removido)
            mostrarlista()
        else:
            print(f'Nenhum produto removido. Lista atual: ')
            mostrarlista()
    elif remover == 'N':
        print('Fim de programa.')
        break
    else:
        print('inválido. Digite [S/N]')
    






