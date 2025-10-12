# Leia nome e media de 1 aluno
# Guarde essa INFO junto a situaçao do aluno(aprovado, reprovado ou em recuperaçao) em 1 dicionario.
# Exibir o resultado nome, media e situação

alunos = dict()

# Cria as KEYS do dict. Os VALUES seram inseridos pelo usuario.
alunos["nome"] = str(input("Nome do aluno: ")).strip().capitalize()
alunos["media"] = float(input("Nota do aluno: "))


# Loop enquanto a nota inserida nao estiver entre 0 e 10.
while alunos["media"] < 0 or alunos["media"] > 10:
    print("-" * 40)
    print("ERROR: Somente notas entre 0 e 10!")
    alunos["media"] = float(input("Nota do aluno: "))

# Condiçoes para cada situaçao do aluno
if 0 < alunos["media"] < 4:
    alunos["situacao"] = "Reprovado."
elif 4 <= alunos["media"] <= 6:
    alunos["situacao"] = "Recuperaçao."
else:
    alunos["situacao"] = "Aprovado."

# For para um print mais organizado.
print("-=" * 10)
for key, value in alunos.items():
    print(f"{key}: {value}")
print("-=" * 10)











