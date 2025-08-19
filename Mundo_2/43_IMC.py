# Ler: Peso, altura e calcule IMC
# Mostre status de acordo com peso
# abaixo de 18.5 abaixo do peso
# entre 18.5 e 25 peso ideal
# 25 a 30 sobrepeso
# 30 a 40 obesidade
# acima de 40 obesidade morbida


print("         Calculo IMC")
print("=-=" * 10)
nome = str(input("Insira seu nome: ")).strip()
peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / (altura * altura)

if imc < 0:
    print("ERROR: VERIFIQUE OS DATOS INSERIDOS!")
elif imc < 18.5:
    print(f"{imc:.2f}: Voce esta abaixo do peso")
elif 18.5 <= imc < 25:
    print(f"{imc:.2f}: Peso ideal")
elif 25 <= imc < 30:
    print(f"{imc:.2f}: Sobrepeso")
elif 30 <= imc < 40:
    print(f"{imc:.2f}: Obesidade")
else:
    print(f"{imc:.2f}: Obesidade morbida")

