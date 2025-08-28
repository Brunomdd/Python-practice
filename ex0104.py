lista = []
cont_provados = 0
cont_reprovados= 0

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) /2
    dados = [nome, [n1, n2], media]
    lista.append(dados)
    resp = ''
    while resp not in ['S', 'N']:
        resp = str(input('Digite [S/N]: ')).strip().upper()
    if resp == 'N':
        break

print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

for i, aluno in enumerate(lista):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    opc = int(input('\nQuer mostrar a nota de qual aluno? (999 Interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(lista):
        print(f'Notas de {lista[opc][0]} são {lista[opc][1][0]} e {lista[opc][1][1]}')
    else:
        print('Número inválido. Tente novamente.')
print(f"Foram cadastrados {len(lista)} alunos")
print('Volte sempre!')
