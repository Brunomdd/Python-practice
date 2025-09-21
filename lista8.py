#Crie um programa que:
#Peça para o usuário digitar a quantidade de alunos.
#Para cada aluno, peça para digitar o nome e a nota (de 0 a 10).
#Armazene os dados em uma lista de listas, onde cada elemento é uma lista com o nome e a nota do aluno.
#Exemplo: [['Ana', 8.5], ['João', 7.0], ...]
#Após a entrada dos dados, mostre:
#A média das notas da turma.
#O nome do aluno com a maior nota.
#O nome do aluno com a menor nota.
#A lista dos alunos que tiraram nota acima da média
s = 0
princ = []
temp = []
maior = 0
menor = 0
menor_nome ='' 
maior_nome = ''
cont  = 0
cont_r = 0

qtd = int(input('Digite a quantidade de alunos: '))
for i in range(0,qtd):
    nome = str(input(f'Digite o nome do {i} aluno: ' ))
    notas = float(input('Digite as notas: '))
    princ.append([nome,notas])
    s += notas

media = s/len(princ)
print(f'a media dos alunos é {media:.2f}')
maior = princ[0][1]
menor = princ[0][1]
maior_nome = princ[0][0]
menor_nome = princ[0][0]
for aluno in princ:
    nome = aluno[0]
    notas = aluno[1]
    if notas > maior:
        maior = notas
        maior_nome = nome
    if notas < menor:
        menor = notas
        menor_nome = nome
print(f'O aluno com a nota mais alta é (o) (a) {maior_nome}')
print(f'O aluno com a nota mais baixa é {menor_nome}')
print('Lista dos alunos acima da média:')
for aluno in princ:
    nome = aluno[0]
    notas = aluno[1]
    if notas > media:
        print(f'{aluno}')


print('Situação dos alunos: ')  
for aluno in princ:
    nome = aluno[0]
    notas = aluno[1]
    if notas >=6.0:     
        cont +=1
        print(f'{nome} - Aprovado')
    else:
        print(f'{nome} - Reprovado')
        cont_r +=1

print(f'Foram aprovados {cont} aluno(s)')
print(f'Foram reprovados {cont_r} aluno(s)')

print(f'Média da turma: {media:.2f}')
print('Alunos com a nota igual a média: ')
for aluno in princ:
    nome  = aluno[0]
    notas = aluno[1]
    if notas == media:
        print(f'{nome} {notas}')

with open('dados_alunos.txt', 'w') as arquivo:
    arquivo.write(f'Média da turma: {media:.2f}\n\n')
    arquivo.write(f'Aluno com a maior nota: {maior_nome} ({maior:.2f})\n')
    arquivo.write(f'Aluno com a menor nota: {menor_nome} ({menor:.2f})\n\n')
    
    arquivo.write('Lista dos alunos acima da média:\n')
    for aluno in princ:
        if aluno[1] > media:
            arquivo.write(f'{aluno[0]} - Nota: {aluno[1]:.2f}\n')

    arquivo.write(f'\nTotal de aprovados: {cont}\n')
    arquivo.write(f'Total de reprovados: {cont_r}\n')

    arquivo.write('\nAlunos com nota igual à média:\n')
    for aluno in princ:
        if aluno[1] == media:
            arquivo.write(f'{aluno[0]} - Nota: {aluno[1]:.2f}\n')

# Agora sim, abrir para ler e mostrar
with open('dados_alunos.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print('Conteúdo do arquivo:')
    print(conteudo)







    
    