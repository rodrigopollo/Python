# Grupo =        0                   1                2
grupos = [['Ana', 'Bruno'], ['Carlos', 'Diana'], ['Eduardo']]
# Aluno =    0       1          0         1           0

# O (i e j) do FOR significa o INDEX (posição)
# GRUPO eh o nome da VAR que escolhi para representar as SUBLISTAS (0, 1, 2)
# ALUNO eh a VAR que representa o conteudo(nomes) dentro das SUBSLITAS

# Vai entrar no GRUPO 0 e depois rodar o 2º FOR para verificar o conteudo dentro do GRUPO 0
# Quando terminar, ele vai pro GRUPO 1 e fazer a mesma coisa. Repeti ate terminar as SUBLISTAS(GRUPO)
for i, grupo in enumerate(grupos):
    print(f'Turma {i}:')

    # Mostra os nomes dos alunos dentro da sublista(GRUPO) atual (0, 1, 2)
    for j, aluno in enumerate(grupo):
        print(f'  Aluno {j}: {aluno}')


"""
- enumerate(grupos) vai percorrer cada grupo da lista GRUPOS e devolver:
- i: o indice de cada grupo (Grupo 0, Grupo 1, Grupo 2)
- grupo: a lista de alunos dentro daquela turma.
"""
