#Exercício Python 026: Faça um programa que leia uma frase pelo teclado
#e mostre quantas vezes aparece a letra "A", em que posição ela aparece
#a primeira vez e em que posição ela aparece a última vez.
# Solicita ao usuário que digite uma frase e realiza algumas transformações na entrada

frase = str(input('Digite uma frase pelo teclado:')).upper().strip()  # Recebe a entrada, converte para maiúsculo e remove espaços extras

# Conta quantas vezes a letra 'A' aparece na frase
print('A letra a aparece {} vezes'.format(frase.count('A')))  # Usa o método count() para contar as ocorrências da letra 'A' na frase

# Encontra a posição da primeira ocorrência da letra 'A' (note que as posições começam de 0, então adiciona 1 para tornar 1-indexed)
print('A letra A aparece na posição {}'.format(frase.find('A')+1))  # O método find() retorna a posição da primeira ocorrência de 'A'. Adiciona-se 1 para a posição começar de 1

# Encontra a posição da última ocorrência da letra 'A' (também começando de 1 para o usuário)
print('A ultima posição que a letra A aparece é {}'.format(frase.rfind('A')+1))  # O método rfind() retorna a posição da última ocorrência de 'A'. Adiciona-se 1 para a posição começar de 1
