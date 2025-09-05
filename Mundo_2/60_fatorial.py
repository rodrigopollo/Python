# Leia 1 numero
# faça o calculo fatoria do numero inserido
# Exemplo: 5 --> 5x4x3x2x1 = 120
from math import factorial

fat = 0
sair = ""
while sair != "S":
    numero = int(input("Digite um numero: "))
    print(factorial(numero))
    sair = str(input("Deseja sair [S/N]")).upper()

#============================
#       ALTERNATIVA
#============================
print("=" * 100)

n = int(input("Digite um numero: "))
contador = n
f = 1

while contador > 0:
    print(f"{n} x {contador} = ")
    f = f * contador
    contador -= 1
