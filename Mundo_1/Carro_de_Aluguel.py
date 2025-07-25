# Pergunte informaçoes sobre um carro alugado e informe quanto deve ser pago:
# Quantos KM voce percorreu?
# Quantos dias voce ficou com o carro? A diaria custa R$60.00
# R$0.15 por cada KM rodado.

dias = int(input("Informe a quantidade de dias que ficou com o carro: "))
km = float(input("Informe quantos KM voce fez com o carro: "))

valorDiaria = 60.00
valorKm = 0.15

totalDiaria = dias * valorDiaria
totalKm = km * valorKm
precoFinal = totalKm + totalDiaria

print(f"\nValor total das diarias = R${totalDiaria:.2f} reais")
print(f"Valor total pelos kilometros percorridos = R${totalKm:.2f} reais")
print(f"\nO valor total a ser pago é de R${precoFinal:.2f} reais.")

