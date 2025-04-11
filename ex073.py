# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.

primeiro = int(input("Digite o primeiro termo da PA: "))
razão = int(input("Digite a razão: "))
cont = 0
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <=total:
        print(f"{primeiro}",end=' ')
        primeiro = primeiro + razão
        cont = cont +1
    mais = int(input("\nQuantos termos a mais deseja mostrar ?: "))

# outra forma também de fazer esse exercício
#p_termo = int(input('Primeiro termo: '))
#razao = int(input('Razão: '))
#c = 10
#while c > 0:
  #  print(p_termo, end=' ')
  #  p_termo += razao
   # c -= 1
   # if c == 0:
       # c = int(input('\nAcrescentar mais números na sequência: '))

# terceira forma de fazer esse exercício
#num = int(input('Digite o número da P.A.: '))
#razão = int(input('Digite a razão da P.A.: '))
#c = 1
#n = 11
#while c < n:
 #   print(num, end=' ')
  #  num += razão
    #c += 1
   # if c == n:
    #    s = int(input('\nQuantos termos a mais deseja ver? Digite 0 para sair.. '))
        #n += s

