# Insira um numero real, e depois mostre como um INT, ou seja, tudo depois da virgula/ponto
# sera cancelado.
# NOTA: Faça importando somente 1 funçao especifica e outra importando a biblioteca inteira.



#                   ------ Importando uma funçao especifica de math ------
from math import trunc

numeroReal = float(input("Insira um numero: "))
numeroInteiro = trunc(numeroReal)

print(f"Voce digitou {numeroReal}.")
print(f"Utilizando o metodo trunc para eliminar as casas decimais = {numeroInteiro}")

#========================================================================================
print("=" * 65)
#========================================================================================

#                   ------ Importando a biblioteca math inteira ------
import math
numeroReal1 = float(input("Insira um numero: "))
numeroInteiro1 = math.trunc(numeroReal1)

print(f"Utilizando o metodo trunc para eliminar as casas decimais = {numeroInteiro1}")


