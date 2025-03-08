#Crie um programa que mostre na tela todos os numeros pares que estão entre 1 e 50.

# Solução 1 (Comentada)
# Abaixo está a solução comentada que percorreria todos os números de 1 a 50
# e verificaria se cada número é par antes de imprimir.

# for i in range (1,50+1):
  #if i % 2 == 0:
     # print('[{}]'.format(i))

# Solução 2 (Economiza menos processador)
# A solução 2 já é otimizada, pois percorre apenas os números pares, sem precisar fazer verificação.

for i in range (2,51,2):
    print('.',end ='')
    print(i,end='')
print('Acabou')





