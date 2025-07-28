# Leia o preço de um produto
# Mostre seu novo valor com 5% de desconto.

produto = float(input("Insira o preço deste produto = R$"))

desconto = produto * 0.05
precoFinal = produto - desconto

print(f"\nO produta custa R${produto:.2f} reais")
print(f"Com o desconto de 5% fica R${precoFinal:.2f} reais")


#       ---------  ALTERNATIVA ---------

desconto = produto - (produto * 0.05)
print("=" * 40)
print(f"O produta custa R${produto:.2f} reais")
print(f"Com o desconto de 5% fica R${desconto:.2f} reais")

