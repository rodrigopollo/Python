# leia o ano de nascimento
# mostre a categoria de acordo com a idade
# ate 9: mirim
# ate 14: infantil
# ate 19 junior
# ate 20 senior
# Acima master

from datetime import date
ano_nasc = int(input("Digite o ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print(f"Voce tem {idade} anos e sua categoria eh --> MIRIM")
elif 10 <= idade <= 14:
    print(f"Voce tem {idade} anos e sua categoria eh --> INFANTIL")
elif 15 <= idade <= 19:
    print(f"Voce tem {idade} anos e sua categoria eh --> JUNIOR")
elif idade == 20:
    print(f"Voce tem {idade} anos e sua categoria eh --> SENIOR")
else:
    print(f"Voce tem mais de {idade} anos e sua categoria eh --> MASTER")

print()

