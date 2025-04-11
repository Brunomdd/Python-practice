# Melhore o ex069, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O Programa encerra quando ele disser que quer mostrar 0 termos.
primeiro = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão da PA: "))

termo = primeiro
cont = 1
total = 0
mais = 10  # Começa mostrando 10 termos

while mais != 0:
    total += mais  # Atualiza o total de termos a serem mostrados
    while cont <= total:
        print(f"{termo}", end=' → ')
        termo += razão
        cont += 1
    print("PAUSA")  # Dá uma pausa para perguntar quantos termos a mais

    mais = int(input("Quantos termos você quer mostrar a mais? (Digite 0 para sair) "))

print("Progressão finalizada com", total, "termos mostrados.")

