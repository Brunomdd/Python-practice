#Crie um programa que:
#Permita cadastrar várias pessoas, guardando para cada uma:
#Nome (string)
#Idade (inteiro)
#Sexo (caractere: 'M' ou 'F')
#Após o cadastro, o programa deve:
#Mostrar quantas pessoas foram cadastradas.
#Calcular e mostrar a média de idade do grupo.
#Listar o nome de todas as mulheres cadastradas.
#Listar todas as pessoas que possuem idade acima da média, exibindo o nome e a idade de cada uma.
#O programa deve permitir que o usuário escolha quando parar de cadastrar pessoas, perguntando a cada vez se deseja continuar.
soma = 0
media = 0
cont_f = 0
pessoas = []
mulheres = []
while True:
    nome = str(input('Digite o nome: '))
    idade = int(input("Digite a idade: "))
    sexo = ''
    while sexo not in ['M', 'F']:
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    pessoa = [nome, idade, sexo]
    pessoas.append(pessoa)
    soma += idade
    if sexo == 'F':
        cont_f +=1
        mulheres.append(nome)
    resp = ''
    while resp not in ['S', 'N']:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
media = soma / len(pessoas)
print(f'\nTotal de pessoas cadastradas: {len(pessoas)}')
print(f'A media de idade das pessoas é {media}')
print(f'Mulheres cadastradas {mulheres}')
print(f'Foram cadastradas {cont_f} mulheres')