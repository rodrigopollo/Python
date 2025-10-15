# Leia, nome do jogador e a quantidade de partidas jogadas.
# Guarde essas informaçoes em 1 dicionario.
# Os gols por partida seram uma lista.
# Quantos gols ele fez em cada partida(Valor independente, ou seja 1 valor por partida.)
# Mostre a info completa e logo em seguida mostre em detalhes os gols por partida e o aproveitamento ao final.

rotulos_para_facil_leitura = {
    "nome": "Nome do jogador",
    "partidas_jogadas": "Partidas jogadas durante o ano",
    "gols_por_partida": "Total de gols marcados por partida",
    "total_gols": "Total de gols feitos durante o ano"
}
# ///////////////////////////////////////////////////////////////////////////////////////////////
#                                   PROGRAMA ABAIXO
# ///////////////////////////////////////////////////////////////////////////////////////////////

# O Dicionario que irei usar, deixando ja criado para facil leitura posterior.
jogador = {"nome": "",
           "partidas_jogadas": 0,
           "gols_por_partida": [],
           "total_gols": 0}

jogador["nome"] = str(input("Nome do jogador: ")).strip().capitalize()

# LOOP que inpede o usuario de inserir numeros negativos, ou seja, impede possiveis erros.
while True:
    jogador["partidas_jogadas"] = int(input("Partidas jogadas: "))
    if jogador["partidas_jogadas"] >= 0:
        break
    else:
        print("ERROR: Valor invalido! Digite um numero maior que ZERO.")
        print("-" * 60)

# LOOP dos numeros de partidas(inserido acima). Inseri quantidade de gols por partida.
for i in range(jogador["partidas_jogadas"]):
    gols = int(input(f"Jogo {i+1}. Quantos gols foram marcados: "))
    jogador["gols_por_partida"].append(gols)

# Soma todos os gols feitos.
jogador["total_gols"]  = sum(jogador["gols_por_partida"])

print(jogador)

# Resultado
# {'nome': 'Paulo gomes', 'partidas_jogadas': 3, 'gols_por_partida': [2, 1, 3], 'total_gols': 6}










