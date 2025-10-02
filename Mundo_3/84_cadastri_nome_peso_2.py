# Uma lista com varias pessoas
# Insira nome e peso por pessoa
# Mostre: Quantas pessoas foram cadastradas
# As pessoas mais pessadas e mas mais leves, top 2 (se for mesmo pesso mostrar as 2 pessoas igual)

dados_pessoas = list()
entrevistados = list()
nomes_MaiorPeso = list()
nomes_MenorPeso = list()
maiorPeso = None
menorPeso = None

while True:
    nome_atual = str(input("Nome: "))
    peso_atual = float(input("Peso: "))

    entrevistados.append([nome_atual, peso_atual])

    # Verificando se o peso do entrevistado eh o maior peso ou eh igual o menor peso.
    if maiorPeso is None:
        maiorPeso = peso_atual
        menorPeso = peso_atual
        nomes_MaiorPeso = [nome_atual]              # Lista com apenas 1 conteudo [string]
        nomes_MenorPeso = [nome_atual]              # Lista com apenas 1 conteudo [string]
        print("maior = ", nomes_MaiorPeso)
        print("menor = ", nomes_MenorPeso)
    else:
        if peso_atual > maiorPeso:
            maiorPeso = peso_atual
            nomes_MaiorPeso = [nome_atual]          # Substitiu o valor de nome_atual dentro da lista.
            print("Maior = ", nomes_MaiorPeso)
        elif peso_atual == maiorPeso:
            nomes_MaiorPeso.append(nome_atual)

        # Se for TRUE, ele muda o valor de menorPeso e altera o nome da lista nomes_MenorPeso..
        if peso_atual < menorPeso:
            menorPeso = peso_atual
            nomes_MenorPeso = [nome_atual]          # Substitiu o valor de nome_atual dentro da lista.
            print("Menor = ", nomes_MenorPeso)      #So para entender como funciona a linha no console.
        elif peso_atual == menorPeso:
            nomes_MenorPeso.append(nome_atual)

    # Condição de saida
    continuar = ""
    while continuar not in ("s", "sim", "n", "nao"):
        continuar = input("Continuar? [S/N]: ").strip().lower()
    if continuar in ("n", "nao"):
        break
    print("-=" * 15)

print("-=" * 30)
print(f"A quantidade de pessoas entrevistadas foi de: {len(entrevistados)}")
print(f"O maior peso foi: {maiorPeso} -> {nomes_MaiorPeso}")
print(f"O menor peso foi: {menorPeso} -> {nomes_MenorPeso}")
print("-=" * 30)












