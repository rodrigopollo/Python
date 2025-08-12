# Programa para comprar 1 casa
# Verificar: Valor da casa, salario do comprador e em quantos anos pretende pagar.
# Calcule a prestaçao mensal, tem q ser <= 30% do salario do comprador.
# Se prestaçao > 30% = negado!

from math import ceil
valor_da_casa = float(input("Qual o valor da casa: "))
salario_comprador = float(input("Qual o seu salario: "))
tempo_para_pagar = float(input("Em quantos anos pretende pagar a casa: "))

qnt_parcelas = tempo_para_pagar * 12
tempo_minimo_aceitavel = valor_da_casa / (salario_comprador * 0.30)
valor_da_parcela = valor_da_casa / qnt_parcelas

if qnt_parcelas < tempo_minimo_aceitavel:
    print(f"NEGADO! Para esta casa voce deve parcelar em no minimo {ceil(tempo_minimo_aceitavel)} vezes.")
elif qnt_parcelas >= tempo_minimo_aceitavel:
    print(f"Voce tera que pagar {qnt_parcelas:.0f} parcelas de R${valor_da_parcela:.2f} para quitar a casa")


# ALTERNATIVA GPT (consultei para verificar possiveis melhorias de claresa de codigo)

from math import ceil

# Entrada de dados
valor_casa = float(input("Qual o valor da casa? R$ "))
salario = float(input("Qual o seu salário? R$ "))
anos_pagamento = int(input("Em quantos anos pretende pagar a casa? "))

# Cálculos
parcelas_totais = anos_pagamento * 12
valor_parcela = valor_casa / parcelas_totais
aprovacao = salario * 0.30
tempo_minimo_necessario = valor_casa / aprovacao

# Decisão
print("-" * 50)
if valor_parcela > aprovacao:
    print("EMPRÉSTIMO NEGADO!")
    print(f"Para essa casa, sua parcela mensal de R${valor_parcela:.2f} excede 30% do seu salário.")
    print(f"Você precisaria de pelo menos {ceil(tempo_minimo_necessario)} parcelas para se enquadrar.")
else:
    print("EMPRÉSTIMO APROVADO!")
    print(f"Você pagará {parcelas_totais} parcelas de R${valor_parcela:.2f}.")
print("-" * 50)

