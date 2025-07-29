# Um programa que sorteie um aluno aleario da classe.,

import random

n1 = "Rodrigo"
n2 = "Ana"
n3 = "Mimmo"
n4 = "Roberto"

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print(f"O aluno escolhido foi: {escolhido}")

# ----- ALTERNATIVA -----
from random import choice

escolhido1 = choice(lista)
print(f"\nAlternativa de escolha: {escolhido1}")



