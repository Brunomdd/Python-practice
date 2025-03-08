#Crie um programa que leia o nome de uma Cidade e diga se ela começa ou não
#Com o nome 'Santo'

# Solicita ao usuário que informe a cidade onde nasceu
cid = str(input('Em que cidade voçe nasceu? : ')).strip()  # A entrada do usuário é convertida para string (redundante) e espaços extras são removidos com .strip()

# Verifica se os primeiros 5 caracteres da cidade (convertidos para maiúsculo) são iguais a "SANTO"
print(cid[:5].upper() == 'SANTO')  # Pega os 5 primeiros caracteres da cidade, os converte para maiúsculo e compara com 'SANTO'.
