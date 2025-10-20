# Leia, nome de varios jogadores e a quantidade de partidas jogadas.
# Guarde essas informaçoes em 1 dicionario.
# Os gols por partida seram uma lista.
# Mostre: a info completa e logo em seguida mostre em detalhes os gols por partida e o aproveitamento ao final.
# Perguntar ao usuario: Qual jogador deseja ver a informaçao completa(numero do indice), 999 = sair

todos_jogadores = []

while True:
    # 1. Cria o dicionário JÁ com a estrutura completa
    jogador = {
        'nome': "",                       # Indica que será preenchido depois
        'total_partidas_jogadas': 0,
        'gols_por_partida': [],              # Cria uma lista vazia
        'total_gols_marcados': 0,
        'media_gols_partida': 0
    }
    # Verifica se o usuario esta inserindo letras. Nao aceita, simbolos, nem numeros e nem nao digitar nada.
    while True:
        nome = input("Nome: ").strip().title()
        nome_sem_espacos = nome.replace(" ", "")
        if nome and nome_sem_espacos.isalpha():
            jogador['nome'] = nome
            break
        print("Digite apenas letras e espaços válidos.")


    # Verifica se o usuario esta digitando somente NUMEROS INTEIROS. Nao aceita letras ou simbolos
    while True:
        try:
            partidas_jogadas = int(input("Partidas jogadas: "))
            if partidas_jogadas > 0:
                jogador['total_partidas_jogadas'] = partidas_jogadas
                break
            else:
                print("ERRO: Somente numero igual ou maiores que Zero.")
        except ValueError:
            print("ERRO: Digite apenas numeros inteiros (ex: 1, 2, 3).")


    # 1) Pede para o usuario os gols marcados em cada partida.
    # 2) Aceita somento numeros e que sejam = ou > 0
    for partida in range(jogador['total_partidas_jogadas']):
        while True:
            try:
                gol = int(input(f"Gols marcados na partida {partida+1}: "))
                if gol >= 0:
                    jogador['gols_por_partida'].append(gol)
                    break
                else:
                    print("ERRO: Somento numeros igual ou maiores que Zero")
            except ValueError:
                print("ERRO: Digite apenas numeros inteiros (ex: 1, 2, 3")


    # Soma todos os gols marcados
    jogador['total_gols_marcados'] = sum(jogador['gols_por_partida'])


    # Media dos gols marcados durante o ano. Caso ZERO partidas, 0 eh media.
    if jogador['total_partidas_jogadas'] > 0:
        media_gols_marcados = jogador['total_gols_marcados'] / jogador['total_partidas_jogadas']
    else:
        media_gols_marcados = 0
    jogador['media_gols_partida'] = media_gols_marcados

    # ADD em uma lista o dicionario com nome, partidas jogadas e gols por partida.
    todos_jogadores.append(jogador.copy())


    # Condiçao de saida do Cadastro
    while True:
        sair = input("Deseja continuar? [S/N]: ").strip().lower()
        if sair in ("s", "sim", "n", "nao"):
            break
        print("Erro: Digite 'S' (sim) ou 'N' (não).")
    if sair in ("n", "nao"):
        break

print("-"*47)
print(f"{'Nº':<3} {'NOME':<15} {'GOLS POR PARTIDA':<20} {'TOTAL':<5}")
print("-"*47)

for i, jogador_atual in enumerate(todos_jogadores, start=1):
    gols_por_partida_string = str(jogador_atual['gols_por_partida'])
    print(f"{i:<3} {jogador_atual['nome']:<15} {gols_por_partida_string:<20} {jogador_atual['total_gols_marcados']:<5}")
print("-"*47)


# Loop para estatisticas de um jogador especifico. Condiçao de saida 999
while True:
    escolha = int(input("De qual jogador voce deseja ver a informaçao completa? (999 para sair): ")) - 1
    if escolha == 998:
        break
    print('-' * 60)

    # Verifica se o numero inserido pelo usuario esta dentro dos indices disponiveis.
    if 0 <= escolha < len(todos_jogadores):
        jogador_selecionado = todos_jogadores[escolha]
        print(f"Estatisticas do jogador {jogador_selecionado['nome']}")

        #
        for partida, gols in enumerate(jogador_selecionado['gols_por_partida'], start=1):
            print(f"  -> Partida {partida}: {gols} gols.")
        print(f"{jogador_selecionado['nome']} teve uma media de {jogador_selecionado['media_gols_partida']} gols por partida este ano")
        print("-=" * 30)
    else:
        print(f"ERRO: Digite um numero de 1 a {len(todos_jogadores)} ou 999 para sair.")

