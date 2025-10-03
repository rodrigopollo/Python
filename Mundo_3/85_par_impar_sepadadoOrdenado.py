# Lista com 7 valores numericos
# Cadastre em uma unica lista.
# Dentro dessa lista, mantenha separao os PARES e IMPARES
# Mostre valores pares e impares em ordem crescente
# DICA: 1 lista com 2 listas dentro. MAS tem que trabalhar so com 1 lista. e nao com 3 e depois juntar.

# Cria as listas PAR e IMPAR e joga dentro de uma lista Composta.
lista_pares = list()
lista_impares = list()
principal = [lista_pares, lista_impares]
# Indice =        0            1

for i in range(7):
    numero = int(input("Digite um Numero: "))

    # Verifica se eh PAR. Si TRUE. Add na lista de pares e organiza.
    if numero % 2 == 0:
        principal[0].append(numero)
        principal[0].sort()

    # Verifica se eh IMPAR. Si TRUE. Add na lista de impares e organiza.
    else:
        principal[1].append(numero)
        principal[1].sort()

    # Condiçao de saiada.
    continuar = ""
    while continuar not in ("s", "sim", "n", "nao"):
        continuar = input("Continuar? [S/N]: ")
    if continuar in ("n", "nao"):
        break
    print("-=" * 10)

print("-=" * 20)
print(f"Numeros pares digitados: {principal[0]}")
print(f"Numeros impares digitados: {principal[1]}")
print("-=" * 20)