# Desenvolva uma lógica que leia o peso e a altura de uma pessoa:
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5:Abaixo do Peso
#Entre 18.5 e 25:Peso ideal
#25 ate 30:Sobrepeso
#30 até 40:Obesidade
#Acima de 40: Obesidade Mórbida

# Solicita o peso ao usuário e converte para tipo float (número decimal)
peso = float(input("Digite o peso: "))

# Solicita a altura ao usuário e converte para tipo float
altura = float(input("Digite a altura: "))

# Calcula o IMC dividindo o peso pelo quadrado da altura
imc = peso / (altura**2)

# Verificando o valor do IMC e classificando de acordo com as faixas
if imc < 18.5:
    # Caso o IMC seja menor que 18.5, a pessoa está abaixo do peso
    print("ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    # Caso o IMC esteja entre 18.5 e 25, a pessoa está no peso ideal
    print("PESO IDEAL")
elif 25 <= imc < 30:
    # Caso o IMC esteja entre 25 e 30, a pessoa está com sobrepeso
    print("SOBREPESO")
elif 30 <= imc < 40:
    # Caso o IMC esteja entre 30 e 40, a pessoa está com obesidade
    print("OBESIDADE")
elif imc > 40:
    # Caso o IMC seja maior que 40, a pessoa está com obesidade mórbida
    print("OBESIDADE MÓRBIDA")
