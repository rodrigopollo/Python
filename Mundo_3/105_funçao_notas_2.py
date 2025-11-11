# Usando funçao faça:
# A funçao vai retornar um dicionario com os seguintes dados:
# - Quantidade de notas, maior nota, menor nota, media da turma, siatuaçao(opcional)
# Add docstrings.

todas_notas = list()

def calculo_notas(notas):
    aluno = dict()

    aluno['quantidade_notas'] = len(notas)
    aluno['maior_nota'] = max(notas)
    aluno['menor_nota'] = min(notas)
    aluno['media_notas'] = sum(notas) / len(notas)
    return aluno

while True:
    nome = input("Digite seu nome: ").strip().title()
    if "".join(nome.split()).isalpha():
        break
    print("Digite apenas letras válidas (sem números ou símbolos).")
    print("-=" * 20)

while True:
    print("-=" * 10)
    print("<< 999 para sair >>")
    nota = float(input('Digite sua nota: '))

    if 0 <= nota <= 10:
        todas_notas.append(nota)
    elif nota == 999:
        break

historico_aluno = calculo_notas(todas_notas)

entrada = input("Deseja ver a situaçao do aluno? [S/N] ").strip().upper()[0]
print("-=" * 20)
print(f"{'Historico do aluno ' + nome:^40}")
print("-=" * 20)

if entrada == 'S':
    if historico_aluno['media_notas'] < 5:
        historico_aluno['siatuacao'] = "Reprovado."
        print(historico_aluno)

    elif 5 <= historico_aluno['media_notas'] < 7:
        historico_aluno['siatuacao'] = "Em recuperaçao."
        print(historico_aluno)
    else:
        historico_aluno['siatuacao'] = "Aprovado."
        print(historico_aluno)
else:
    print(historico_aluno)


