
# Um programa que leia largura e altura de 1 parede em m²
# Calcule a area e a quantidade de tinta necessaria (1 litro cada 2m²)

altura = float(input("Insira a altura da parede: "))
largura = float(input("Insira a largura da parede: "))

area = altura * largura
tinta = area / 2

print(f"A parede tem {area:.2f}m² e vai precisar de {tinta:.1f} litros de tinta para pintar")