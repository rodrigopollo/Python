

catetoOposto = float(input("Cateto oposto: "))
catetoAdjacente = float(input("Cateto adjacente: "))

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print(f"A hipotenusa mede {hipotenusa:.2f}")

# ALTERNATIVA
from math import hypot

hipotenusa = hypot(catetoOposto, catetoAdjacente)
print(f"\nCalculo alternativo {hipotenusa:.2f}")
