# O programa vai gerar 1 numero aleatio entre 1 e 5
# VOce vai tentar adivinhar
# Retorna a resposta si voce acertou ou nao.

from random import choice
from time import sleep

numero_Aleatorio = random.randint(1, 5)
sua_Escolha = int(input("Adivinhe o numero: "))

if sua_Escolha == numero_Aleatorio:
    print("WTF, voce realmente acertou!?")
else:
    print("muahaha, siga tentando meu joven padawan")
    print(f"O numero era {numero_Aleatorio}")

