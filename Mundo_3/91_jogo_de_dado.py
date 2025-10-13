# Nenhum dado sera inserido. 4 jogadores vao jogar o dado.
# Guarde o resultado em um dicionario.
# Mostre os numeros dos dados em ordem e o vencedor com o maior numero.
# Colocar um delay entre os dados jogados e sorteados.

from random import randint
from operator import itemgetter

jogadores = dict()

# Cria as KEYS dentro de JOGADORES e randomiza o VALUE com randint.
jogadores["Jogador1"] = randint(1, 6)
jogadores["Jogador2"] = randint(1, 6)
jogadores["Jogador3"] = randint(1, 6)
jogadores["Jogador4"] = randint(1, 6)

# Tranforma o dicionario em TUPLAS e organiza do MAIOR para o MENOR.
ranking_jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

# FOR para percorrer as tuplas e pegar NOME e VALOR de cada JOGADOR e mostrar na tela.
for index, (nome, valor) in enumerate(ranking_jogadores, start=1):
    print(f"{index}º) Lugar:")
    print(f"      {nome:} com o numero {valor}")







