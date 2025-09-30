#Faça um programa que tenha uma função chamada escreva (), Que receba um texto qualquer como parametro e mostre uma mensagem como 
#tamanho adaptável

def escreva(msg):
    tam = len(msg) +4
    print('~' * tam) 
    print(f'  {msg}  ')
    print('~' * tam)
  
while True:
    texto = str(input('Digite um texto para sair digite [Sair]:'))
    if texto.lower() == 'sair':
        break
    escreva(texto)
print('Fim de programa')
    

 