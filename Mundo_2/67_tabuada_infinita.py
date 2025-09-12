# Leia um numero INT
# Mostre a tabuada e repita
# Condiçao de saida = numero negativo.

print("=" * 50)
print(f"{"Tabuada infinita":^50}")
print("=" * 50)
contador = resultado = 0

numero = int(input("Qual tabuada voce quer ver: "))

while True:
    if numero < 0:
        print("=" * 30)
        print("Obrigado por usar o programa!")
        print("=" * 30)
        break

    contador += 1
    if 0 < contador <= 10:
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")
    if contador > 10:
        contador = 0
        numero = int(input("\nQual tabuada voce quer ver: "))










