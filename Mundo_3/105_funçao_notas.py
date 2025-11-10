# Usando funçao faça:
# A funçao vai retornar um dicionario com os seguintes dados:
# - Quantidade de notas, maior nota, menor nota, media da turma, siatuaçao(opcional)
# Add docstrings.

# Personal idea

def quantidade_notas(notas):
    return len(notas)


def maior_nota(notas):
    return max(notas)


def menor_nota(notas):
    return min(notas)


def media_notas(notas):
    return sum(notas) / len(notas)


# Programa Principal
todas_notas = list()

while True:
    nome = input("Digite seu nome: ").strip().title()
    if "".join(nome.split()).isalpha():
        break
    print("Digite apenas letras válidas (sem números ou símbolos).")
    print("-=" * 20)

contador = 1
while True:
    print("-=" * 10)
    print("<< 999 para sair >>")
    nota = float(input(f"Digite a {contador}º nota: "))

    if 0 <= nota <= 10:
        todas_notas.append(nota)
    elif nota == 999:
        break

quantidade_notas(todas_notas)
maior_nota(todas_notas)
menor_nota(todas_notas)
media_notas(todas_notas)

entrada = input("Deseja ver a situaçao do aluno? [S/N] ").strip().upper()[0]
print("-=" * 20)
print(f"{'Historico do aluno ' + nome:^40}")
print("-=" * 20)
print(f"Foram inseridas {quantidade_notas(todas_notas)} nota(s)")
print(f"Maior nota: {maior_nota(todas_notas)}")
print(f"Menor nota: {menor_nota(todas_notas)}")

if entrada == 'S':
    if media_notas(todas_notas) < 5:
        print(f"Media das notas: {media_notas(todas_notas):.1f}, Reprovado!")
    elif 5 <= media_notas(todas_notas) < 7:
        print(f"Media das notas: {media_notas(todas_notas):.1f}, Recuperaçao!")
    else:
        print(f"Media das notas: {media_notas(todas_notas):.1f}, Aprovado!")
else:
    print(f"Media das notas: {media_notas(todas_notas):.1f}")

















