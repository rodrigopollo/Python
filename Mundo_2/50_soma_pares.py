# Insira 6 numeros inteiros
# Some somente os pares

# Variaveis de start
contador = 0
soma = 0

# Condiçao
for i in range(1, 7):
    numero = int(input(f"Digite o {i}º numero: "))
    if numero < 0:
        print("ERROR: NUMERO INVALIDO")
        exit()
    elif numero % 2 == 0:
        soma += numero
        contador += 1

# Decisao
print("-=" * 25)
print(f"A soma dos {contador} numeros pares inseridos eh de {soma}")
print("-=" * 25)