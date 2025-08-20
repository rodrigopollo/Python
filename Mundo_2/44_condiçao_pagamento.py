# Calcule o valor pago dependendo do modo de pagamento
# A vista dinheiro ou cheque 10% desconto
# a vista cartao 5%
# 2x preço nomral
# 3x ou mais 20% juros

valor_a_pagar = float(input("Qual o valor a pagar: "))

if valor_a_pagar < 0:
    print("ERROR: VALOR INVALIDO!")
    exit()

print("=-=" * 20)
print("   METODO DE PAGAMENTO")
print("[1] - A vista no dinheiro ou cheque.")
print("[2] - A vista no cartao.")
print("[3] - 2x no cartao")
print("[4] - 3x ou mais no cartato")
print("=-=" * 20)

escolha = int(input("Insira o metodo de pagamento que deseja usar: "))

m1 = valor_a_pagar - (valor_a_pagar * 0.10)
m2 = valor_a_pagar - (valor_a_pagar * 0.05)
m3 = valor_a_pagar
m4 = valor_a_pagar + (valor_a_pagar * 0.20)

if escolha == 1:
    print(f"A vista no dinheiro ou cheque fica --> {m1}")
elif escolha == 2:
    print(f"A visa no cartao fica --> R${m2}")
elif escolha == 3:
    dois_parcelas = m3 / 2
    print(f"Voce tera que pagar 2x parcelas de R${dois_parcelas}")
elif escolha == 4:
    qnt_parcelas = int(input("Insira a quantidade de parcelas desejadas: "))
    valor_parcela = m4 / qnt_parcelas
    print(f"Voce tera que pagar {qnt_parcelas} parcelas de R${valor_parcela} com juros")
else:
    print("ERROR: METODO DE PAGAMENTO ESCOLHIDO INVALIDO")

