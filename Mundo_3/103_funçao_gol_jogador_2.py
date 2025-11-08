# Usando funçao
# Preenche o nome e gols marcados pelo jogador
# Deve aceitar Nome e/ou gols VAZIOS (nesse caso Nome: Desconhecido e GOL zero)

def dados_jogador(nome, gols):
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f"{nome} fez {gols} gol(s) no campeonato.")

# Caos nao seja digitado nada, nome recebera valor DESCONHECIDO em vez de VAZIO("") como paramentro.
nome_jogador = input("Digite o nome do jogador: ").strip().capitalize()
if nome_jogador == "":
    nome_jogador = "<Desconhecido>"

# Qualquer valor abaixo de ZERO sera transformado em ZERO.
gols_marcados = input("Gols marcados: ")
if gols_marcados.isnumeric():
    gols_marcados = int(gols_marcados)
else:
    gols_marcados = 0

dados_jogador(nome_jogador, gols_marcados)


