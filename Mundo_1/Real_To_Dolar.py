
# Insira um valor float (dinheiro) em reais R$
# Diga quantos dolares a pessoa consegue comprar com esse dinheiro.

reais = float(input("Quanto dinheiro voce tem? = "))

dolar = reais / 5.42

print(f"Com R${reais:.2f} reais voce consegue comprar ${dolar:.2f} dolars.")