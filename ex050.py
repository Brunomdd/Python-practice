
t1 = 1  # Inicializa t1 com 1 (primeiro número da sequência de Fibonacci)
print(t1)  # Exibe o valor de t1 (1)

t2 = 1  # Inicializa t2 com 1 (segundo número da sequência de Fibonacci)
print(t2)  # Exibe o valor de t2 (1)

# Laço para calcular os próximos números da sequência de Fibonacci
for i in range(2, 15):  # Começa de 2, porque os dois primeiros números (1 e 1) já foram exibidos
    t3 = t1 + t2  # Calcula o próximo número da sequência (t3 = t1 + t2)
    print(t3)  # Exibe o valor de t3 (próximo número da sequência)

    t1 = t2  # Atualiza t1 para o valor de t2 (preparando para o próximo cálculo)
    t2 = t3  # Atualiza t2 para o valor de t3 (preparando para o próximo cálculo)
