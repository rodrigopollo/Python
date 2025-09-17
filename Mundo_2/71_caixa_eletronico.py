# Pergunte, qual o valor quer retirar (INT)
# O programa devera informar quantas notas de cada valor seram entregues.
# O caixa tem notas de 1, 10, 20 e 50.

from math import floor

n1 = 50
n2 = 20
n3 = 10
n4 = 1

print("=" * 40)
print("Caixa Eletrônico".center(40))
print("=" * 40)

while True:
    saque = int(input("Qual o valor que deseja retirar: "))
    print("-" * 40)

    sobra = saque  # começa com o valor total digitado

    # Notas de R$50
    notas50 = floor(sobra / n1)
    sobra -= notas50 * n1
    if notas50 > 0:
        print(f"Você retirou {notas50} notas de R${n1:.2f}")

    # Notas de R$20
    notas20 = floor(sobra / n2)
    sobra -= notas20 * n2
    if notas20 > 0:
        print(f"Você retirou {notas20} notas de R${n2:.2f}")

    # Notas de R$10
    notas10 = floor(sobra / n3)
    sobra -= notas10 * n3
    if notas10 > 0:
        print(f"Você retirou {notas10} notas de R${n3:.2f}")

    # Notas de R$1
    notas1 = floor(sobra / n4)
    sobra -= notas1 * n4
    if notas1 > 0:
        print(f"Você retirou {notas1} notas de R${n4:.2f}")

    break










