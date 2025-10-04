# Um programa que cria uma matrix 3x3
# Preencha com os valores lidos.
# Mostrar na tela o desenho da matris ja preenchida com os valores inseridos.


# lista = [1] [2] [3]......... exemplo de lista visual do quero fazer.

numeros_matrix = list()
temp_list = list()

# Faz o loop 9x e cada numero inserido eh adicionado na LISTA
while 9 > len(numeros_matrix):
    numero = int(input("Digite um numero: "))
    numeros_matrix.append([numero])

# Imprimi a lista ja com formato de matrix 3x3
print(numeros_matrix[0], numeros_matrix[1], numeros_matrix[2])
print(numeros_matrix[3], numeros_matrix[4], numeros_matrix[5])
print(numeros_matrix[6], numeros_matrix[7], numeros_matrix[8])

