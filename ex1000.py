nomes = []
notas = []

for i in range(2):  # coloque 5 se quiser 5 alunos
    nomes.append(input('Nome: '))
    notas.append(float(input('Nota: ')))

media = sum(notas) / len(notas)
print(f'Média da turma: {media:.2f}')

# Maior e menor nota e o aluno correspondente
print(f'Maior nota: {nomes[notas.index(max(notas))]} - {max(notas)}')
print(f'Menor nota: {nomes[notas.index(min(notas))]} - {min(notas)}')

# Alunos acima da média
for i in range(len(notas)):
    if notas[i] > media:
        print(f'{nomes[i]} está acima da média')