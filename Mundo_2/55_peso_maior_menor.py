# Leia peso de 5 pessoas
# Mostre o maior e o menor.

maior_peso = 0
menor_peso = 0

for i in range(1, 4):
    peso = float(input("Insira o peso: "))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso < menor_peso:
            menor_peso = peso
        elif peso > maior_peso:
            maior_peso = peso

print("-=" * 20)
print("    O maior e o menor peso sao:")
print("-=" * 20)
print(maior_peso)
print(menor_peso)


