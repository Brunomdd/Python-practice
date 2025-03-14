# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até dar um valor correto.


# solicita a entrada do usuário
sexo = input("\033[30mDigite o sexo [M/F]: ").strip().upper()[0] # remove os espaços deixa as letras em maisculas e vai mostrar a letra sempre na posição 0 que no caso é o [M]

# loop while para verificar se sexo for diferente de masculino e o sexo for diferente de feminino
while sexo != 'M' and sexo != 'F':

    # se nenhuma das condições for atendida, vai mostrar um erro falando para tentar novamente
    print("\033[31mentrada errada tente novamente: ")

    # solicita a entrada do usuário para verificar novamente
    sexo = input("\033[30mDigite o sexo M para masculino ou F para feminino: ").strip().upper()[0]
print(f"\033[36mSexo {sexo} registrado com sucesso, Usuário registrado com sucesso!") # mostra que o usuário foi registrado com sucesso se a condição for atentida





