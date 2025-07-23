
# Crie um algaritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input("Insira o numero desejado: "))

dobro = n1 * 2
triplo = n1 * 3
raizQuadrada = n1 ** (1/2)

print(f"Dobro de {n1} = {dobro}")
print(f"Triplo de {n1} = {triplo}")
print(f"Raiz quadrada de {n1:.2f} = {raizQuadrada}")