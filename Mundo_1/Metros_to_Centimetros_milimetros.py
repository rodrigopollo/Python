
#Escreva um programa que leia um valor em metros e mostre quantos centimetros e milimitros
# sao o equivalante ao valor inserido.

metros = float(input("Quantos metros voce precisa? = "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"Voce disse que precisa de {metros}m²")
print(f"{metros}m² sao o equivalente a {centimetros:.0f}cm")
print(f"{metros}m² sao o equivalente a {milimetros:.0f}ml")