# Aprimore o exercicio 86
# Mostre a soma dos valores pares
# A soma da terceira coluna
# O maior valor da segunda linha.

num_matrix = list()
soma_par = 0
soma_impar = 0
soma_coluna = 0
maior_numero = 0

# Loop para rodar 9x para depois colocar em uma matrix 3x3
while 9 > len(num_matrix):
    numero = int(input("Digite um numero: "))
    num_matrix.append(numero)

    # Detecta qual numero inserido eh PAR ou IMPAR, SOMA e armazena na VAR.
    if numero % 2 == 0:
        soma_par += numero
    else:
        soma_impar += numero

    # Pega os ultimos numeros de cada COLUNA DA MATRIX e soma.
    if len(num_matrix) % 3 == 0:
        soma_coluna += numero

# Verifica qual o maior NUMERO inserido na 2º COLUNA da MATRIX.
# Start indice 1, percorra a lita inteira, pulo os proximos 2 valores e verifique o terceiro valor da lista.
# ira verificar 1, 4, 7.
for indice in range(1, len(num_matrix), 3):
    if num_matrix[indice] > maior_numero:
        maior_numero = num_matrix[indice]

# Print da matrix 3x3
print(f"[{num_matrix[0]}] [{num_matrix[1]}] [{num_matrix[2]}]")
print(f"[{num_matrix[3]}] [{num_matrix[4]}] [{num_matrix[5]}]")
print(f"[{num_matrix[6]}] [{num_matrix[7]}] [{num_matrix[8]}]", "\n")

print(f"Soma dos pares: {soma_par}")
print(f"Soma impares: {soma_impar}")
print(f"Soma da 3º coluna = {soma_coluna}")
print(f"Maior numero da 2º coluna: {maior_numero}")


#    ALTERNATIVA PARA VERIICAR SEGUNDA COLUNA

# for indice in [1, 4, 7]:
#     if num_matrix[indice] > maior_numero:
#         maior_numero = num_matrix[indice]

