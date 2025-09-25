# Leia 5 numeros e guarde eles em uma lista.
# Mostre o MAIOR e o MENOR valor digitado e suas posiçoes na lista.
# Caso o numero se repita, mostrar em quais posiçoes estao os 2 numeros.


numero = list()
maior = menor = index_maior = index_menor = 0

# Loop para inserir 5 numeros na lista
for i in range(5):
    numero.append(int(input(f"Digite um numero para a posiçao {i}: ")))

    # Cria a variavel com o maior e menor numeros da lista.
    maior = max(numero)
    menor = min(numero)

    # Cria a variavel para o INDEX dos mior e menor numero da lista.
    index_maior = numero.index(maior)
    index_menor = numero.index(menor)

print("-=" * 20)
print(f"Numeros digitados: {numero}")
print(f"Maior numero digitado: posiçao {index_maior}: {maior}")
print(f"Menor numero digitado: posiçao {index_menor}: {menor}")
print("-=" * 20)


#======================================================================
#                          ALTERNATIVA
#======================================================================

print("\n")
print("-=" * 30)
print("ALTERNATIVA".center(30))
print("-=" * 30)

listanum = list()
mai = men = 0
for i in range(5):
    listanum.append(int(input(f"Digite um valor para a Posiçao {i}: ")))

    if i == 0:
        mai = listanum[i]
        men = listanum[i]
    else:
        if listanum[i] > mai:
            mai = listanum[i]
        if listanum[i] < men:
            men = listanum[i]

print("-=" * 30)
print(f"Voce digitou os valores {listanum}")

print(f"Maior valor: {mai} nas posiçoes ", end="")
for index, numero in enumerate(listanum):
    if numero == mai:
        print(f"{index}...", end="")

print(f"\nMenor valor: {men} nas posiçoes ", end="")
for index, numero in enumerate(listanum):
    if numero == men:
        print(f"{index}...", end="")

print("\n" + "-=" * 30)









