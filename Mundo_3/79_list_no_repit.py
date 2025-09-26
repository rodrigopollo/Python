# Leia os numeros ate o usuario querer parar.
# Cadastre esses numeros em 1 list.
# Caso o numero se repita, nao sera adicionado.
# Mostre a lista em ordem crescente.
#///////////////////////////////////////////////////////////////////////////////////////////////////////
numeros = list()

# Loop de verificação de LISTA
while True:
    print("-=" * 15)
    valor = int(input("Digite um numero: "))

    # Verifica se o valor inserido ja existe na lista
    if valor in numeros:
        print("Numero Invalid: Ja existe na lista")
    else:
        numeros.append(valor)
        print("Numero valido, adicionado na lista")

    # Comando de saida, se o usuario digitar qualquer coisa q nao seja S ou N o programa avisa.
    while True:
        sair = input("Deseja continuar? [S/N]: ").strip().upper()

        if sair in ("S", "SIM", "NAO", "N"):
            break
        else:
            print("Apenas S ou N.")
    if sair in ("N", "NAO"):
        break
# Mostra a lista digitado e altera ela de maneira ordenada.
print(f"Os numeros digitados foram: {numeros}")
numeros.sort()
print(f"Organizados em ordem crescente: {numeros}")

