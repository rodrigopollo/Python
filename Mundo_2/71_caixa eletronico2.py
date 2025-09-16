# Pergunte, qual o valor quer retirar (INT)
# O programa devera informar quantas notas de cada valor seram entregues.
# O caixa tem notas de 1, 10, 20 e 50.

cinquenta = 50
vinte = 20
dez = 10
um = 1

print("=" * 40)
print("Caixa Eletrônico".center(40))
print("=" * 40)

while True:
    saque = int(input("Qual o valor que deseja retirar: "))

    sobra = saque
    # Voce zera as variaveis para que qndo o loop se repita (se repetir) os valores zerem.
    notas50 = notas20 = notas10 = notas1 = 0

    while sobra >= cinquenta:
        sobra -= cinquenta
        notas50 += 1
    while sobra >= vinte:
        sobra -= vinte
        notas20 += 1
    while sobra >= dez:
        sobra -= dez
        notas10 += 1
    while 0 < sobra < 10:
        sobra -= um
        notas1 += 1

    print(f"\nVoce retirou R${saque:.2f} do caixa eletronico.")
    print(f"Sendo: {notas50:.2f} notas de R${cinquenta:.2f}")
    print(f"Sendo: {notas20:.2f} notas de R${vinte:.2f}")
    print(f"Sendo: {notas10:.2f} notas de R${dez:.2f}")
    print(f"Sendo: {notas1:.2f} notas de R${um:.2f}")
    print("-" * 40)

    break


