# Digite 2 numeros inteiros
# Compare e diga, qual eh maior ou se tem o mesmo valor.


print("   DIGITE 2 NUMEROS INTEIROS")
print("=" * 30)
n1 = int(input("1º numero: "))
n2 = int(input("2º nuemro: "))

print("-" * 25)
if n1 > n2:
    print(f"O maior numero eh o {n1}")
elif n1 == n2:
    print("Os dois numeros sao iguais.")
else:
    print(f"O maior numero eh o {n2}")
print("-" * 25)

