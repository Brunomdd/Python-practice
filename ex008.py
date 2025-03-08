#Escreva um programa que leia um valor em metros e o exiba convertido em
# milímmetros

# Solicita ao usuário que digite uma distância em metros e converte para um número de ponto flutuante
metros = float(input('Uma distância em metros: '))

# Calcula a distância em centímetros (1 metro = 100 centímetros)
cm = metros * 100

# Calcula a distância em milímetros (1 metro = 1000 milímetros)
mm = metros * 1000

# Exibe os resultados formatados, mostrando a distância original em metros, e as conversões para centímetros e milímetros
print('A medida de {}m corresponde a {}cm e {}mm'.format(metros, cm, mm))
# A função 'format()' substitui as chaves {} pelos valores das variáveis 'metros', 'cm' e 'mm'.
