# Leia 3 numeros e diga qual o Maior e qual o Menor

n1 = int(input("1º numero: "))
n2 = int(input("2º numero: "))
n3 = int(input("3º numero: "))

if n1 > n2 and n1 > n3:
    print(f"O maior numero eh o {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior numero eh o {n2}")
else:
    print(f"O maior numero eh o {n3}")

if n1 < n2 and n1 < n3:
    print(f"{n1} eh o menor numero")
elif n2 < n1 and n2 < n3:
    print(f"{n2} eh o menor numero")
else:
    print(f"{n3} eh o menor numero")

# ALTERNATIVA

