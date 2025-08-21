# jokenpo

import random
from time import sleep

print(f"{" JOKENPO ":=^40}")
print("""Suas opçoes:
[0] - Pedra.
[1] - Papel.
[2] - Tesoura.
""")

itens = ("PEDRA", "PAPEL", "TESOURA")
computador = random.randint(0, 2)

jogador = int(input("Pedra, papel ou tesoura: "))

if jogador not in [0, 1, 2]:
    print("ERRO: OPÇAO INVALIDA!")
    exit()

print("Jo...")
sleep(0.5)
print("ken...")
sleep(0.5)
print("po...")

print("-=" * 11)
print(f"Computador jogou {itens[jogador]}")
print(f"Voce jogou {itens[computador]}")
print("-=" * 11)

if computador == jogador:
    print("Empate!")
elif (computador == 0 and jogador == 1) or \
        (computador == 1 and jogador == 2) or \
            (computador == 2 and jogador == 0):
            print("Voce ganhou!")
else:
    print("Voce Perdeu!")













