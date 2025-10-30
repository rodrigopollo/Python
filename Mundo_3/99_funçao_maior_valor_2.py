# Crie uma funçao que receba varios parameters INT (nao sera INPUT)
# Mostre: Quantos numeros foram inseridos e qual foi o maior valor.
# NOTE: Caso valores seja VAZIO ou negativo, devera mostrar ZERO.

def verifica_maior_valor(*valores):
    maior_valor = 0
    len_verifica_maior_valor = len(valores)

    # FOR para mostras os valores inseridos e a quantidade de entradas.
    for valor in valores:
        print(valor, end=' ')
    print(f"Foram inseridos {len_verifica_maior_valor} valores.")

    # Verifica qual o maior numero inserido
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
    print(f"Maior valor: {maior_valor}")
    print('-=' * 20)

verifica_maior_valor(2, 9, 4, 5, 7)
verifica_maior_valor(4, 7, 0)
verifica_maior_valor(2)
verifica_maior_valor(0)
verifica_maior_valor(-100)
verifica_maior_valor()


















