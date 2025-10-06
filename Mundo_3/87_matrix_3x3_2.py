# Um programa que cria uma matrix 3x3
# Preencha com os valores lidos.
# Mostrar na tela o desenho da matris ja preenchida com os valores inseridos.
# Mostre a soma dos valores pares
# A soma da terceira coluna
# O maior valor da segunda linha.


# qnt_sublista =          0           1           2
matriz =             [[0, 0, 0],  [0, 0, 0],  [0, 0, 0]]
# conteudo_interno =   0  1  2     0  1  2     0  1  2

soma_par = 0
soma_coluna = 0
maiorValor_SegundaColuna = 0

# FOR para setar os valores nas sublistas dentro da Lista Principal MATRIZ
for qnt_sublista in range(len(matriz)):
    for conteudo_Interno in range(len(matriz)):
        matriz[qnt_sublista][conteudo_Interno] = int(input("Digite um numero: "))

        if matriz[qnt_sublista][conteudo_Interno] % 2 == 0:
            soma_par += matriz[qnt_sublista][conteudo_Interno]


# Percorre as 3 sublistas pegando so o ultimo VALOR de cada uma = [[_, _, 0],  [_, _, 0],  [_, _, 0]]
for conteudo_Interno in range(0, 3):
    soma_coluna += matriz[conteudo_Interno][2]


# Percorre a segunda coluna da MATRIZ e verifica qual o maior valor dentro dela.
for conteudo_Interno in range(0, 3):
    if matriz[conteudo_Interno][1] > maiorValor_SegundaColuna:
        maiorValor_SegundaColuna = matriz[conteudo_Interno][1]


# FOR para IMPRIMIR em formato 3x3 os valores das sublistas dentro da LISTA MATRIZ
print("-=" * 30)
for qnt_sublista in range(len(matriz)):
    for conteudo_Interno in range(len(matriz)):
        print(f"[{matriz[qnt_sublista][conteudo_Interno]:^5}]", end="")
    print()


print("-=" * 30)
print(f"Soma dos pares: {soma_par}")
print(f"Soma da 3º coluna = {soma_coluna}")
print(f"Maior numero da 2º coluna: {maiorValor_SegundaColuna}")
print("-=" * 30)




""" Explicaçao detalhada do FOR IT (for dentro de for)"""

    # qnt_sublista =                 0           1           2
    # matriz =                  [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
    # conteudo_interno =          0  1  2     0  1  2     0  1  2


    # FOR EXTERNA: Quantas sublistas existem dentro da lista.
    #   -->   for qnt_lista in range(matriz):

    # O FOR EXTERNO, vai percorer o indice da lista, ou seja, quantas sublistas (lista dentro de lista)
    # tem dentro da lista principal MATRIZ. Nesse caso sao 3, entao ele vai percorer 0, 1, 2.
    # Entao o for externo vai percorer 3x ja que so tem 3 sublistas, ou seja, 3 indeces.

    # FOR INTERNA: Quantos elementos na sublista atual.
    #   -->   for conteudo_Interno in range(matriz):

    # O FOR INTERNO, vai percorer cada valor interno das 3 SUBLISTAS que existem dentro da MATRIZ.
    # ou seja, 3 listas com 3 valores. O for interno vai percorer entao 3 valores dentro de cada sublista.
    # Entao o for interno vai percorrer 9x porque sao 3 valores dentro de 3 sublistas. (3x3)

