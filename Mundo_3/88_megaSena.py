# O programa pede quantos jogos da megasena vc quer geral.
# Vai sortear 6 numeros aleatorios entre 1 e 60 pra cada jogo
# Nao pode repetir os numeros dentro do mesmo jogo

from random import randint

jogos = int(input("Insira o numero de jogos a sortear: "))
contador = 0
print("-=" * 18)
# Enquanto o contador nao for = ao numero inserido em JOGOS, o loop continua.
while contador != jogos:
    contador += 1

    # Lista vazia criada para armazenar os numeros sorteados por cada loop.
    # Lembrando que lista criada sem setar valores, para LEN vale 0
    sorteio = []

    # Enquanto a lista Sorteio nao tiver 6 numeros o loop continuara.
    while len(sorteio) < 6:

        # Sorteio numeros aleatorios e armazena dentro da lista SORTEIO.
        numeros_Sorteados = randint(1, 60)

        # Adiciona o numero sorteado na lista ""SE"" ainda nao existir dentro da LISTA.
        if numeros_Sorteados not in sorteio:
            sorteio.append(numeros_Sorteados)

    print(f"{contador}ª sorteio: {sorteio}")
print("-=" * 18)







