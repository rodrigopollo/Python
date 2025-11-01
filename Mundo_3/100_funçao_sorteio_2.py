# Crie uma lista
# Funçao 1: Vai sortear 5 numeros e colocar na lista (0 a 10)
# Funçao 2: Vai somar todos os numeros pares sorteados.
# Mostre: A lista sorteada
# Mostre: Os numeros pares e o resultado da soma

from random import randint


def sorteio(a: int, b: int, qtd: int = 5):
    return [randint(a, b) for _ in range(qtd)]

def numeros_pares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    return pares, sum(pares)

numeros = sorteio(1, 10)
pares, soma = numeros_pares(numeros)
print(f"Números sorteados: {numeros}")
print(f"Números pares: {pares}")
print(f"Soma dos pares: {soma}")
