# Leia varios numeros coloque em 1 lista
# Mostre quantos numeros foram digitados
# A lista em ordem decrescente
# Se o valor 5 foi digitado e esta ou nao na lista
# Opcional (mostrar o index de 5)

list_numeros = list()
index_cinco = []
while True:

    # Le um numero e insere dentro da lista com o metodo APPEND(). Append add no final da lista.
    valor = int(input("Digite um numero: "))
    list_numeros.append(valor)

    # Verifica qnts numeros 5 tem na lista e guardo o index dele
    cinco = list_numeros.count(5)

    for index, numero in enumerate(list_numeros):      # percorre a lista e olha o index e número
        if numero == 5:                                # se o número for 5
            if index not in index_cinco:               # e esse index ainda não foi adicionado a index_cinco
                index_cinco.append(index)              # adiciona o index na lista

    # Condiçao para sair do programa.
    while True:
        sair = str(input("Exit [S/N]: ")).strip().upper()
        print("-=" * 20)

        if sair in ("S", "SIM", "N", "NAO"):
            break
        else:
            print("ERRO: Digite apenas uma das opçoes: S, SIM, N, NAO")
            print("-=" * 20)
    if sair in ("S", "SIM"):
        break


print("-=" * 20)
print(f"Os numeros digitados foram: {list_numeros}")
print(f"Foram digitados {len(list_numeros)} numeros")
print(f"Total de numeros 5 na lista: {cinco}")
if index_cinco:
    print(f"O numero 5 se encontra nos index: {index_cinco}")
else:
    print("O numero 5 nao foi digitado em nenhum index")

list_numeros.sort(reverse=True)
print(f"Em ordem descrescente: {list_numeros}")
print("-=" * 20)



