# Insira data de nascimento
# Se ele ainda vai se alistar pro serviço militar
# Se deve se alistar esse ano
# se ja passou o ano de se alistar

from datetime import date
ano_nascimento = int(input("Digite seu ano de nascimento: "))

# aqui vc esta pegando so o ano da data atual, sendo assim se torna INTEIRO e verificando idade atual
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
idade_alistamento =  18

if idade == idade_alistamento:
    print(f"Agora que voce tem {idade} anos chegou a hora de se alistar no exercito, nao esqueça!")
elif idade < idade_alistamento:
    anos_ate_alistamento = idade_alistamento - idade
    print(f"Voce ainda tem {idade} anos e tem {anos_ate_alistamento} ate que precise se alistar")
else:
    alistamento_atrasado = idade - idade_alistamento
    print(f"Voce ja tem {idade} anos e teria que ter se alistado a {alistamento_atrasado} anos.")


# ALTERNATIVA
print("=" * 60)
atual = date.today().year
nascimento = int(input("Digite seu ano de nascimento: "))
idade = atual - nascimento

if idade == 18:
    print(f"Agora que voce tem {idade} anos chegou a hora de se alistar no exercito, nao esqueça!")
elif idade < 18:
    saldo = 18 - idade
    print(f"Voce ainda tem {idade} anos e tem {saldo} ate que precise se alistar")
elif idade > 18:
    saldo = idade - 18
    print(f"Voce ja tem {idade} anos e teria que ter se alistado a {saldo} anos.")
