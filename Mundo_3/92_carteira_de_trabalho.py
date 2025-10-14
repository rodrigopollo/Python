# Leia: nome, ano de nascimento
# Coloque em um Dicionario (a idade sera cadastrada e nao o ano de nascimento, calcule e resolva)
# Leia: Se a carteira de trabalho for 0 pule a questao de contratos e nao mostre (coloque qualquer numero)
# Leia: Ano de contrataçao e salario.
# Mostre: na tala as informaçoes e com quantos anos a pessoa pode se aposentar.
# NOTE: Aposenta depois e 35 anos de trabalho

from datetime import date

entrevistados = dict()
data = date.today().year

entrevistados["Nome"] = str(input("Nome: ")).strip().capitalize()
entrevistados["Idade"] = int(input("Ano de nascimento: "))
entrevistados["CTPS"] = int(input("Carteira de Trabalho (0 se nao tem): "))

if entrevistados["CTPS"] != 0:
    entrevistados["Contratado"] = int(input("Ano de Contrataçao: "))
    entrevistados["Salario"] = int(input("Salario: R$"))

entrevistados["Aposentadoria"] = (entrevistados["Contratado"] + 35) - entrevistados["Idade"]

# Calcula a idade atual do entevistado atraves do ano de nascimento.
if entrevistados["Idade"] > 0:
    entrevistados["Idade"] = data - entrevistados["Idade"]

print("=" * 40)
for key, value in entrevistados.items():
    print(f"{key}: {value}")

print("=" * 40)











