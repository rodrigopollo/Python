# Crie uma tupla com os 20 primeiros colocados do Brasileirao na ordem de colocaçao
# Mostre apenas os 5 primeiros
# Mostre os ultimos 4
# Mostre em ordem alfabetica
# Em que posiçao da tabela esta o time do Mirassol.


times = ("Cruzeiro", "Flamengo", "Bragantino", "Bahia", "Palmeiras",  "Botafogo", "Mirassol",
         "Fluminense", "Atletico-MG", "Corinthians", "Ceara SC", "Gremio", "Sao Paulo")

print("=" * 60)
print(f" --- OS 5 PRIMEIROS COLOCADOS DO BRASILEIRAO SAO ---".center(55))
print("=" * 60)
print(f"{times[:5]}\n")

print("=" * 60)
print(f" --- OS 4 ULTIMOS COLOCADOS DO BRASILEIRAO SAO ---".center(55))
print("=" * 60)
print(f"{times[-4:]}\n")

print("=" * 60)
print(f" --- OS TIMES NO BRASILEIRAO EM ORDEM ALFABETICA ---".center(55))
print("=" * 60)
print(f"{sorted(times)}\n")

print("=" * 60)
print(f" --- POSICAO DO MIRASSOL NA TABELA ---".center(55))
print("=" * 60)
print(f"O Mirassol esta na {times.index("Mirassol") + 1}º posiçao")


