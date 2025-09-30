# Leia varios numeros e coloque em 1 lista
# Crie outras 2 listas, 1) com os PARES, 2) com os IMPARES
# Mostre as 3 listas.,

# Criaçao das listas que seram usadas no programa.
numeros = list()
par = list()
impar = list()

# Loop infinito para inserir valores e verificar em qual lista devem estar.
while True:
    valor = int(input("Digite um numero: "))
    numeros.append(valor)

    # Condiçao para verificar se o numero inserido eh par ou impar.
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    # Condiçao de saida do programa.
    while True:
        sair = input("Deseja Continuar [S/N]: ").strip().upper()
        print("-=" * 12)

        if sair in ("S", "Sim", "N", "Nao"):
            break
        else:
            print("-> Digite apenas S ou N")
            print("-=" * 12)

    if sair in ("N", "Nao"):
        break

# Imprimi respostas diferentes dependendo de se teve ou nao teve numeros pares e impares digitados.
print("-=" * 20)
print(f"Numeros digitados: {numeros}")
if par:
    print(f"Os pares da lista sao: {par}")
else:
    print("A lista nao contem numeros pares.")

if impar:
    print(f"Os impares da lista sao: {impar}")
else:
    print("A lista nao contem numeros impares")
print("-=" * 20)
