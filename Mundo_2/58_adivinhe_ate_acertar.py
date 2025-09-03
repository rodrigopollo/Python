# Exercicio 28 melhorado
# O computador vai pensar em 1 numero e voce vai ter que adivinhar
# Agora o jogo de adivinha so vai terminar qndo vc acertar o numero.

from random import randint

print("-=" * 20)
print(f"{'Adivinha o Numero':^40}")
print("-=" * 20)

numero_a_adivinhar = randint(1, 10)
escolha_jogador = 0
while numero_a_adivinhar != escolha_jogador:
    escolha_jogador = int(input("Qual o numero: "))
    if escolha_jogador == numero_a_adivinhar:
        print("Parabens, voce acertou!")
    elif escolha_jogador < numero_a_adivinhar:
        print("Eh um numero maior")
        print("-" * 26)
    elif escolha_jogador > numero_a_adivinhar:
        print("Eh um numero menor")
        print("-" * 26)




