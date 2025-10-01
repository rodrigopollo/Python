# Uma lista com varias pessoas
# Insira nome e peso por pessoa
# Mostre: Quantas pessoas foram cadastradas
# As pessoas mais pessadas e mas mais leves, top 2 (se for mesmo pesso mostrar as 2 pessoas igual)

entrevistados = []
pessoa_maiorPeso = []
pessoa_menorPeso = []
maior_peso = 0
menor_peso = 0
contador = 0
dados_pessoasTemporario = []

while True:
    contador += 1
    dados_pessoasTemporario.clear()  # limpa a lista antes de adicionar dados
    print(f"Candidato {contador}")

    # Insere temporariamente um NOME e um PESO e logo enseguida copia para a lista ENTREVISTADOS
    dados_pessoasTemporario.append(str(input("Nome: ")))
    dados_pessoasTemporario.append(float(input("Peso: ")))

    entrevistados.append(dados_pessoasTemporario[:])        # [nome, peso]

    # Cria VARIAVEIS temporarias para usar como PARAMETRO para os calculos abaixo.
    nome_atual = dados_pessoasTemporario[0]
    peso_atual = dados_pessoasTemporario[1]

    # Na 1º, sempre vdd. Seta as VAR de maior e menor peso e o nome dessas pessoas.
    if peso_atual > maior_peso:
        maior_peso = menor_peso = peso_atual
        pessoa_maiorPeso = [nome_atual]
        pessoa_menorPeso = [nome_atual]

    # Verifica se o novo peso inserio eh maior ou menor do que os SETADOS ACIMA. Substitui se TRUE.
    else:
        if peso_atual > maior_peso:
            maior_peso = peso_atual
            pessoa_maiorPeso = [nome_atual]
        elif peso_atual < menor_peso:
            menor_peso = peso_atual
            pessoa_menorPeso = [nome_atual]

        # Verifica se alguem tem o mesmo peso do MAIOR OU MENOR peso e adiciona se TRUE.
        else:
            # adiciona empatados com maior ou menor peso
            if peso_atual == maior_peso:
                pessoa_maiorPeso.append(nome_atual)
            if peso_atual == menor_peso:
                pessoa_menorPeso.append(nome_atual)
    # Condiçao de saida
    while True:
        sair = input("Continuar? [S/N]: ").strip().lower()
        if sair in ("s", "sim", "n", "nao"):
            break
        print("Digite apenas S ou N.")
    if sair in ("n", "nao"):
        break
    print("-=" * 15)

print("-=" * 30)
print(f"A quantidade de pessoas entrevistadas foi de: {len(entrevistados)}")
print(f"O maior peso foi: {maior_peso} -> {pessoa_maiorPeso}")
print(f"O menor peso foi: {menor_peso} -> {pessoa_menorPeso}")
print("-=" * 30)













