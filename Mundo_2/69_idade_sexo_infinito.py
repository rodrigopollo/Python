# Leia idade e sexo de varias pessoas. Perguntar se quer continuar ou nao.
# Se a resposta do sexo for errada, perguntar novamente.
# Quantas pessoas > 18 anos
# Quantos homens
# Quantas mulheres < 20 anos.

adultos = homens = mulheres = 0

while True:

    idade = int(input("Qual a idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual o genero [M/F]: ")).strip().upper()[0]

    if idade > 18:
        adultos += 1
    if idade < 20 and sexo.upper() == "F":
        mulheres += 1
    if sexo.upper() == "M":
        homens += 1

    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Continuar: [S/N]: ")).strip().upper()
    if continuar == "N":
        break

print(f"{adultos} pessoas sao maiores de 18 anos.")
print(f"{homens} homens foram registrados.")
print(f"{mulheres} muheres com menos de 20 anos foram registradas.")





