# Leia um numero inteiro e diga se ele eh um numero primo ou nao
# NOTE: numeros primos sao dividos por 1 e por ele mesmo e nada mais.
# Use FOR

# Info + Entrada de dados
print(f"{" Identificador de numeros primos ":-^50}")
print("Para deixar o programa digite 0 (zero)\n")

numero = int(input("Digite um numero: "))
contador = 0

# Condiçao 1
for i in range(1, numero +1):
    if numero == 0:
        print("Obrigado por usar nosso programa.")
        exit()
    elif numero % i == 0:
        contador += 1

# Condiçao 2
if  contador == 2:
    print(f"O numero {numero} eh PRIMO ")
elif contador != 2:
    print(f"O numero {numero} nao eh PRIMO")


# ===========================================
# | ALTERNATIVA  --> Minha resposta original|
# ===========================================


print("=" * 80)
numero = int(input("Digite um numero: "))

# Condiçao e Decisao
for i in range(2, numero +1):
    if numero == 0:
        print("Obrigado por usar nosso programa.")
        exit()
    elif numero % i == 0:
        print("n eh primo")
        exit()
    else:
        print(f"primo.")
        exit()
print()



