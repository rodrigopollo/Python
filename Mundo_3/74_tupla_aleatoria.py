# Gere 5 numeros aleatorios e adicione em 1 TUPLA
# mostre os numeoros gerados.
# Qual foi o maior numero e qual o menor.

from random import randint

aleatorio = (randint(1, 11), randint(1, 11), randint(1, 11), randint(1, 11),
             randint(1, 11))

# Mostra o valor armazenado em cada INDEX
print("-=" * 15)
print("--- Numeros sorteados ---".center(20))
for i in aleatorio:
    print(f"{i}", end=" ")

print("\n")
print("-=" * 15)
print(f"Maior valor sorteado foi: {max(aleatorio)}\n")

print("-=" * 15)
print(f"Menor valor sorteado foi: {min(aleatorio)}")


