# Crie uma funçao que receba varios parameters INT (nao sera INPUT)
# Mostre: Quantos numeros foram inseridos e qual foi o maior valor.
# NOTE: Caso valores seja VAZIO ou negativo, devera mostrar ZERO.

def verificar_maior_valor(*valores):
    maior_valor = 0
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
    print(f"Maior valor: {maior_valor}")


verificar_maior_valor(2, 9, 4, 5, 7)
verificar_maior_valor(4, 7, 0)
verificar_maior_valor(2)
verificar_maior_valor(0)
verificar_maior_valor(-100)
verificar_maior_valor()
























