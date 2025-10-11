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
    media = (nota1 + nota2) / 2
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

# Para cada SUBLISTA(aluno) dentro de ALUNOS, me motre o NOME e a MEDIA de cada aluno.
for index, aluno in enumerate(alunos):
    print(f"{index:<5}{aluno[0]:<15}{media:>6}")
print("-" * 27, "\n")

# Mostra as nota de um aluno escolhido atraves do seu INDICE(numero) ou sai do programa com 999.
while True:
    condicao_de_saida = int(input("Mostrar nota de qual aluno? (999 para SAIR): "))
    if condicao_de_saida == 999:
        break
    else:
        if 0 <= condicao_de_saida < len(alunos):
            print(f"{alunos[condicao_de_saida]}")
            print("-" * 60)
        else:
            print("Numero invalido, tente novamente")






