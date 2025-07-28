# Insira um numero
# Mostre a tabuada do numero inserido

tabuado = int(input("Insira o numero que deseja ver a tabauada: "))

for i in range(1, 11):
    resultado = tabuado * i
    print(f"{tabuado} x {i} = {resultado}")
print("=" * 12)


#       ----------  ALTERNATIVA  ---------

print(f"{tabuado} x 1 = {tabuado * 1}")
print(f"{tabuado} x 2 = {tabuado * 2}")
print(f"{tabuado} x 1 = {tabuado * 3}")
print(f"{tabuado} x 1 = {tabuado * 4}")
print(f"{tabuado} x 1 = {tabuado * 5}")
print(f"{tabuado} x 1 = {tabuado * 6}")
print(f"{tabuado} x 1 = {tabuado * 7}")
print(f"{tabuado} x 1 = {tabuado * 8}")
print(f"{tabuado} x 1 = {tabuado * 9}")
print(f"{tabuado} x 1 = {tabuado * 10}")