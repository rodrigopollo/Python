# Insira um numero
# Retorne a resposta, eh par ou impar

numero = int(input("Digite um numero: "))

par_Impar = numero % 2

if par_Impar == 0:
    print("O numero eh par.")
else:
    print("O numero eh impar.")

