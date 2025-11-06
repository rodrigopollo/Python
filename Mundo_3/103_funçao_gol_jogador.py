# Usando funçao
# Preenche o nome e gols marcados pelo jogador
# Deve aceitar Nome e/ou gols VAZIOS (nesse caso Nome: Desconhecido e GOL zero)


def dados_jogador(gols_jogador_atual):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{nome_jogador} fez {gols_jogador_atual} gol(s) no campeonato.")

# Caos nao seja digitado nada, nome recebera valor DESCONHECIDO
nome_jogador = input("Digite o nome do jogador: ").strip().capitalize()
if nome_jogador is None or nome_jogador == "":
    nome_jogador = "<Desconhecido>"
else:
    nome_jogador = nome_jogador

# Qualquer valor abaixo de ZERO sera transformado em ZERO.
gols_marcados = input("Gols marcados: ")
if gols_marcados == "":
    gols_marcados = 0

dados_jogador(gols_marcados)

















