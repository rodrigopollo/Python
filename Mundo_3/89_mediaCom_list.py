# Leia Nome e 2 notas de varios alunos
# Guarde em uma lista composta (lista dentro de lista)
# Mostre a media de cada aluno com nome e media
# Perguntar se o usuario quer ver todas as notas de um aluno especifico
# Criar uma saida pra isso tbm. (EX: SAIR, 999 etc..) comando de saida.



# Alunos = [ ["Ana", 7.5, 8],  ["Pedro", 6.3, 7 ],   ["Joao", 6,7, 5.5]  ]
# Index =           0                   1                     2

# Aluno =   ["Ana", 7.5, 8],  ["Pedro", 6.3, 7 ],   ["Joao", 6,7, 5.5]
# Index =      0     1   2        0      1   2         0      1     2


alunos = list()
media = 0

while True:
    nome_digitado = str(input("Nome: ")).strip().capitalize()
    nota1 = float(input("Nota: "))
    nota2 = float(input("Nota: "))

    alunos.append([nome_digitado, nota1, nota2])

    # Condiçao de saida
    continuar = ""
    while continuar not in ("sim", "s", "nao", "n"):
        continuar = str(input("Continuar? [S/N]: ")).strip().lower()
    if continuar in ("nao", "n"):
            break

# Forma uma tabela para deixar mais bonito no console
print("-" * 27)
print(f"{"No.":<5}{"Nome":<15}{"Media":>6}")
print("-" * 27)

# Para cada SUBLISTA dentro de ALUNOS, pega o NOME e as 2 NOTAS e coloca em VARIAVEIS. Faz a mesdia tbm.
for index, aluno in enumerate(alunos):  #Lista principal contem os ALUNOS e suas NOTAS.
    nome_na_sublist = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    media = (aluno[1] + aluno[2]) / 2
    print(f"{index:<5}{nome_na_sublist:<15}{media:>6}")
print("-" * 27, "\n")


# Mostra as nota de um aluno escolhido ou sai do programa.
while True:
    condicao_de_saida = int(input("Numero do aluno para ver as notas ou 999 para SAIR: "))
    if condicao_de_saida == 999:
        break
    else:
        if 0 <= condicao_de_saida < len(alunos):
            print(f"{alunos[condicao_de_saida]}")
            print("-" * 60)
        else:
            print(f"Somente numero de 0 a {len(alunos)}")








