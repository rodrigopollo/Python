# Uma funçao que vai receber o ano de nascimento
# Return: retorna a situaçao dessa pessoa (pode votar, voto opicinal ou ainda nao pode votar)

from datetime import date


def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade


nome = input("Digite seu nome: ").strip().title()
ano_nascimento_usuario = int(input("Digite o ano de nascimento: "))

idade = calcular_idade(ano_nascimento_usuario)

if idade >= 18:
    print(f"{nome} tem {idade} anos e pode votar.")
elif 16 <= idade < 18:
    print(f"{nome} tem {idade} anos e tem voto opcional.")
else:
    print(f"{nome} tem {idade} anos e ainda não pode votar.")
