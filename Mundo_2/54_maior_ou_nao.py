# Leia o ano de nascimento de 5 pessoas.
# mostre quem ainda nao eh maior de idade e quem ja.

maior_idade = 0
menor_idade = 0

for i in range(0, 1):
    nome = str(input("Digite um nome: ")).strip()
    idade = int(input("Digite a idade: "))
    print("-" * 20)
    if idade <= 0:
        print("ERROR: IDADE INVALIDA! (A IDADE TEM QUE SER MAIOR QUE 0)")
        exit()
    elif idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

# Decisao
print(f"De todas as pessoas intrevistadas {maior_idade} sao maiores de idade")
print(f"De todas as pessoas intrevistadas {menor_idade} sao menores de idade")

#=============================
#      Alternativa
#=============================

print("=" * 60)

from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for i in range(0, 2):
    nome1 = str(input("Nome: "))
    nascimento = int(input("Ano de nascimento: "))
    idade1 = ano_atual - nascimento

    if nascimento < 0:
        print("ERROR: IDADE INVALIDA")
        exit()
    elif idade1 >= 18:
        maior += 1
    else:
        menor += 1

print(f"Dos intrevistados {maior} pessoas sao maiores de idade")
print(f"Dos intrevistados {menor} pessoas sao menores de idade")







