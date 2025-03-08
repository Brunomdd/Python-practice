# Solicita o tipo de carro alugado, pode ser "Popular" ou "Luxo"
carro = str(input(("Que tipo de carro alugou? [Popular/Luxo]: ")))

# Solicita o número de dias de aluguel
dias = int(input("Por quantos dias alugou?:"))

# Solicita a quilometragem percorrida pelo carro
km = float(input("Kilometros percorridos: "))

# Se o carro for "popular" e a quilometragem for até 100 km, aplica o valor de R$0,20 por km
if carro == "popular" and (km <=100):
    valor_pago = (km*0.20) + (dias*90)  # Calcula o valor para carros populares com até 100 km

# Se o carro for "popular" e a quilometragem for maior que 100 km, aplica o valor de R$0,10 por km
elif carro == "popular" and km >100:
    valor_pago =(km * 0.10) + (dias * 90)  # Calcula o valor para carros populares com mais de 100 km

# Se o carro for "luxo" e a quilometragem for até 200 km, aplica o valor de R$0,30 por km
elif carro == "luxo"and km <= 200:
    valor_pago = (km * 0.30) + (dias * 150)  # Calcula o valor para carros de luxo com até 200 km

# Se o carro for "luxo" e a quilometragem for maior que 200 km, aplica o valor de R$0,25 por km
elif  carro == "luxo" and (km > 200):
    valor_pago = (km * 0.25) + (dias * 150)  # Calcula o valor para carros de luxo com mais de 200 km

# Exibe o valor a ser pago, formatado com 2 casas decimais
print("Valor a ser pago: R$ {:.2f}".format(valor_pago))  # Exibe o valor final com 2 casas decimais
