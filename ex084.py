##Crie uma tupla preeenchida com os 20 primeiros colocados na tabela do campeonado Brasileiro de futebol
#Na ordem da colocação. Depois mostre:
#Os 5 primeiros
#B Os últimos 4 colocados.
#C Times em ordem aflabética.
#D Em que posição está o time do Mirassol FC.

times = (
    "Flamengo",
    "Cruzeiro",
    "Red Bull Bragantino SP",
    "Palmeiras SP",
    "Fluminense RJ",
    "Botafogo FR RJ",
    "Bahia",
    "Mirassol FC",
    "Atletico Mineiro MG",
    "Ceará SC CE",
    "Corinthians SP",
    "Gremio",
    "São Paulo FC SP",
    "Internacional RS",
    "Vasco Gama",
    "EC Vitória BA",
    "Fortaleza CE",
    "Santos FC SP",
    "EC Juventude RS",
    "Recife",
)

print(f"Lista de times do campeonato de futebol {times}")
print(f"\nOs 5 primeiros são: {times[0:5]}")
print('-='*15)
print(f'\nos 4 ultimos são: {times[-4:]}')
print('-='*15)
print(f'\ntimes em ordem alfabetica {sorted(times)}')
print(f'Mirassol FC está ná {times.index('Mirassol FC')+1} posição')
print(f'inversao {times[4::-1]}')
print('')




