
# Turma =        0                   1                2
turmas = [['Ana', 'Bruno'], ['Carlos', 'Diana'], ['Eduardo']]
# Aluno =    0       1          2         3           4

# Pra cada turma
for turma in turmas:     # Sublist 0, 1, 2
    for aluno in turma:  # Pra cada Aluno 0 a 4 dentro da Sublista Turma 0, 1, 2
        print(aluno)     # Me mostre cada Nome de Aluno

numeros = [[1, 2], [3, 4], [5, 6]]

for numero in numeros:
    for valor in numero:
        print(valor)

""" Explicaçao detalhada do FOR IT (for dentro de for)"""

# qnt_sublista =                 0           1           2
# matriz =                  [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
# conteudo_interno =          0  1  2     0  1  2     0  1  2


# FOR EXTERNA: Quantas sublistas existem dentro da lista.
#   -->   for qnt_lista in range(len(matriz)):

# O FOR EXTERNO, vai percorer o indice da lista, ou seja, quantas sublistas (lista dentro de lista)
# tem dentro da lista principal MATRIZ.
# Entao o for externo vai percorer 3x ja que so tem 3 sublistas, ou seja, 3 indeces [0, 1, 2]

# FOR INTERNA: Quantos elementos na sublista atual.
#   -->   for conteudo_Interno in range(len(matriz)):

# O FOR INTERNO, vai percorer cada valor INTERNO dentro das SUBLISTAS dentro da LISTA MATRIZ.
# Ou seja, 3 sublistas com 3 valores cada uma.
# Entao o for interno vai percorer os 3 valores dentro de cada uma das sublistas. 3 por sublista.
# Ou seja, o for interno vai percorrer 9x, 3 valores dentro de 3 sublistas.
# [0, 1, 2], [0, 1, 2], [0, 1, 2]

# Como sao 2 FOR um dentro do outro. O programa funciona da seguinte maneira:

# PRIMEIRO FOR  -->     for qnt_lista in range(len(matriz)):
# SEGUNDO FOR   -->        for conteudo_Interno in range(len(matriz)):


# Oq queremos? ler os valores dentro de cada sublista. OK
# Quantas sublistas temos? = 3
# Quantos valores temos dentro de cada sublista? = 3

# SIGNIFICADO DO FOR:
                # for qnt_lista          -->   Veja cada indice
                # in range(len(matriz))  -->   dentro da lista MATRIZ. Depois do ultimo indice finalize.
                # Ai voce coloque oq ele faz qndo ele leer, print, outra condiçao etc.

# Sabendo isso oq o primeiro e o segundo for estao fazendo?

# for qnt_lista in range(len(matriz)):
#    for conteudo_Interno in range(len(matriz)):
#       print(f"Sublista = {qnt_lista} : índice interno = {conteudo_Interno} : valor = {matriz[qnt_lista][conteudo_Interno]}")

# PRIMEIRO FOR  -->  Para cada indice dentro da lista MATRIZ
# SEGUNDO FOR   -->  Percorra o conteudo dentro do indice atual(sublista atual), ou seja,
# 0 = [0, 1, 2]...... 1 = [0, 1, 2]..... 2 = [0, 1, 2]
# O Resultado visual basicamente seria isso daqui.

""" LISTA ATUAL PARA NAO ESQUECER E PODER VERIFICAR COM O RESUTLADO"""
# qnt_sublista =                 0           1           2
# matriz =                  [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
# conteudo_interno =          0  1  2     0  1  2     0  1  2


# Sublista = 0 : índice interno = 0 : valor = 1
# Sublista = 0 : índice interno = 1 : valor = 2
# Sublista = 0 : índice interno = 2 : valor = 3
# Sublista = 1 : índice interno = 0 : valor = 4
# Sublista = 1 : índice interno = 1 : valor = 5
# Sublista = 1 : índice interno = 2 : valor = 6
# Sublista = 2 : índice interno = 0 : valor = 7
# Sublista = 2 : índice interno = 1 : valor = 8
# Sublista = 2 : índice interno = 2 : valor = 9