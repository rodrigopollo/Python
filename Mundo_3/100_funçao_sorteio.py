# Crie uma lista
# Funçao 1: Vai sortear 5 numeros e colocar na lista (0 a 10)
# Funçao 2: Vai somar todos os numeros pares sorteados.
# Mostre: A lista sorteada
# Mostre: Os numeros pares e o resultado da soma

from random import randint

numeros_sorteados = list()
numeros_pares_sorteados = list()

# FUNÇAO: Sorteia 5 numeros aleatorios entre 1 e 10 e armazena em uma lista
def sorteio(a, b):
    for i in range(5):
        sorteio_de_numeros = randint(a, b)
        numeros_sorteados.append(sorteio_de_numeros)
    print(f"Os numeros sorteados foram {numeros_sorteados}.")


# FUNÇAO: Verifica e mostra para o usuarios os numeros pares sorteados e a soma deles.
def numeros_pares(*numeros):
    soma_pares = 0
    for numero in numeros_sorteados:
        if numero % 2 == 0:
            soma_pares += numero
            numeros_pares_sorteados.append(numero)
    print(f"Os numeros pares sorteados foram {numeros_pares_sorteados}.")
    print(f"A soma dos numeros pares = {soma_pares}")

sorteio(1, 10)
numeros_pares(numeros_sorteados)



