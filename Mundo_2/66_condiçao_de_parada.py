# Leia varios numeros INT
# Condiçao de parada 999
# Mostre --> Quantos numeros foram digitados e a soma deles.
# Desconsuderar o FLAG (999)

contador = soma = 0

print("-" * 50)
print(f"{"Digite 999 para sair":^50}")
print("-" * 50)

while True:
    numero = int(input("Digite um numero: "))

    if numero != 999:
        contador += 1
        soma += numero
    else:
        if contador == 1 and numero == 999:
            print("-" * 40)
            print("\nNao existe soma ou contador de numeros digitados pois so foi digitado 1 numero.")
            print("Obrigado por usar nosso programa!")
            break
        else:
            print("=" * 40)
            print(f"Foram digitados {contador} numeros")
            print(f"A soma dos numeros digitados eh igual a {soma}")
            print("=" * 40)

            print("Obrigado por usar nosso programa.")
            break


#========================
#      ALTERNATIVA
#========================


soma1 = cont = 0

while True:
    num = int(input("Digite um valor (999 para sair): "))
    if num == 999:
        break
    cont += 1
    soma += num
print(f"A soma dos {cont} valores foi {soma1}")

