# Jogue par ou impar com o programa
# O jogo termina quando o jogador PERDER
# No final mostre qntas vitorias consecutivas o Jogador teve.

from random import randint

print("=" * 50)
print(f"{"Jogo do Par ou Impar":^50}")
print("=" * 50)

escolha = vitoria = 0

while True:
    escolha = str(input("Par ou Impar: ")).strip().upper()
    numero = int(input("Escolha um numero entre 0 e 10: "))
    computador = randint(0, 11)

    if numero < 0 or numero > 10:
        print("ERROR: NUMERO INVALIDO, DIGITE UM NUMERO ENTRE 1 E 10")
        break
    if numero > computador:
        maior = numero
        resultado = maior - computador
    else:
        menor = numero
        resultado = computador - menor

    if resultado % 2 == 0:
        print(f"O computador escolheu {computador}. Voce venceu")
        vitoria += 1
    else:
        print(f"O computador escolheu {computador}. Voce perdeu")
        print(f"GAME OVER! Voce venceu {vitoria} vezes seguidas.")
        break


