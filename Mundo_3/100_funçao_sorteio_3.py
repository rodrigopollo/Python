# Crie uma lista
# Funçao 1: Vai sortear 5 numeros e colocar na lista (0 a 10)
# Funçao 2: Vai somar todos os numeros pares sorteados.
# Mostre: A lista sorteada
# Mostre: Os numeros pares e o resultado da soma

from random import randint
numeros_sorteados = list()

def sorteia(numeros):
    for contador in range(5):
        numeros_aleatorios = randint(1, 10)
        numeros.append(numeros_aleatorios)
        print(f"{numeros_aleatorios}", end=' ')


def soma_par(numeros_pares):
    soma_dos_numeros_pares = 0
    for numero in numeros_pares:
        if numero % 2 == 0:
            soma_dos_numeros_pares += numero
    print(f"--> Soma dos numeros pares: {soma_dos_numeros_pares}")


sorteia(numeros_sorteados)
soma_par(numeros_sorteados)





