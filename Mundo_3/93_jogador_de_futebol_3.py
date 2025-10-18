# Tentar chegar em algo assim.

# Paulo Gomes jogou 3 esta temporada.
# Na 1º partida, Paulo gomes fez 2 gols.
# Na 2º partida, Paulo gomes fez 3 gols.
# Na 3º partida, Paulo gomes fez 0 gols.
# Na 4º partida, Paulo gomes fez 1 gols.
# Na 5º partida, Paulo gomes fez 1 gols.
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Paulo gomes fez um total de 7 em 5 partidas.
# A media de gols dele esse ano foi de -> 1.4 gols por partida.
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# VERSAO 3

rotulos_para_facil_leitura = {
                            "nome": "Nome do jogador",    #1)
                            "partidas_jogadas": "Partidas jogadas durante o ano",   #2)
                            "gols_por_partida": "Quantidade de gols marcados por partida",   #3)
                            "total_gols": "Total de gols feitos durante o ano"     #4)
                             }
# ///////////////////////////////////////////////////////////////////////////////////////////////
#                                   PROGRAMA ABAIXO
# ///////////////////////////////////////////////////////////////////////////////////////////////


# O Dicionario que irei usar, deixando ja criado para facil leitura posterior.
jogador = {"nome": "",
           "partidas_jogadas": 0,
           "gols_por_partida": [],
           "total_gols": 0}

jogador["nome"] = str(input("Nome do jogador: ")).strip().title()

# LOOP que inpede o usuario de inserir numeros negativos, ou seja, impede possiveis erros.
while True:
    jogador["partidas_jogadas"] = int(input("Partidas jogadas: "))
    if jogador["partidas_jogadas"] >= 0:
        break
    else:
        print("ERROR: Valor invalido! Digite um numero igual ou maior que ZERO.")
        print("-" * 60)

# LOOP dos numeros de partidas(inserido acima). Inseri quantidade de gols por partida.
for i in range(jogador["partidas_jogadas"]):
    gols = int(input(f"Jogo {i+1}. Quantos gols foram marcados: "))
    jogador["gols_por_partida"].append(gols)

# Soma todos os gols feitos e verifica o aproveitamento do jogador durante o ANO.
jogador["total_gols"]  = sum(jogador["gols_por_partida"])
aproveitamento = jogador["total_gols"] / jogador["partidas_jogadas"]

# Mostrando ao usuario o resultado.
print("-" * 36)

print(f"{jogador["nome"]} jogou {jogador["partidas_jogadas"]} esta temporada.")
for i in range(jogador["partidas_jogadas"]):
    print(f" -> Na {i+1}º partida, {jogador[f"nome"]} fez {jogador["gols_por_partida"][i]} gols.")

print("\n" + "-=" * 30)
print(f"{jogador['nome']} fez um total de {jogador["total_gols"]} gols em {jogador["partidas_jogadas"]} partidas.")
print(f"Media de gols do jogador no final da temporada:  {aproveitamento:.2f} gols por partida.")
print("-=" * 30)

# Resultado

# Paulo Gomes jogou 3 esta temporada.
#  -> Na 1º partida, Paulo Gomes fez 2 gols.
#  -> Na 2º partida, Paulo Gomes fez 3 gols.
#  -> Na 3º partida, Paulo Gomes fez 1 gols.
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Paulo Gomes fez um total de 6 em 3 partidas.
# Media de gols do jogador no final da temporada: 2.00 gols por partida.
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
