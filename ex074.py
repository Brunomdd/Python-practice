# Solicita ao usuário a quantidade de termos que deseja exibir
num = int(input("Quantos termos quer mostrar? "))
# Inicializa os dois primeiros termos da sequência
t1 = 0
print(t1, end=' ')  # Exibe o primeiro termo
t2 = 1
print(t2, end=' ')  # Exibe o segundo termo

# Variável de controle do loop, começando do terceiro termo
cont = 3
while cont <= num:  # Enquanto não atingir a quantidade desejada de termos
    t3 = t1 + t2  # Calcula o próximo termo da sequência
    print(t3, end=' ')  # Exibe o termo gerado
    t1 = t2  # Atualiza o primeiro termo
    t2 = t3  # Atualiza o segundo termo
    cont += 1  # Incrementa o contador para continuar o loop

print()  # Pula para a próxima linha ao final da execução do while

# Segunda forma de fazer usando o loop for

# Solicita  ao usuário a quantidade de termos
num = int(input("Digite os termos fibonacci: "))

# Inicializa os dois primeiros termos da sequência
t1 = 0
print(t1, end=' ')  # Exibe o primeiro termo
t2 = 1
print(t2, end=' ')  # Exibe o segundo termo

# Utiliza um loop for para calcular os termos da sequência
for i in range(3, num + 1):  # Começa do terceiro termo até o número informado pelo usuário
    t3 = t1 + t2  # Calcula o próximo termo da sequência
    t1 = t2  # Atualiza o primeiro termo
    t2 = t3  # Atualiza o segundo termo
    print(t3, end=' ')  # Exibe o termo gerado

print()  # Pula para a próxima linha ao final da execução do for
