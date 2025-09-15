# Leia o nome e preço dos produtos varias vezes. (Isso eh uma compra Ex: mercado)
# Perguntar se quer continuar ou nao. Se digitar errado S ou N, perguntar novamente
# Qual o gasto total da compra
# Quantos produtos custam mais de R$1.000,00
# Qual eh o nome do produto mais barato.

gasto_tot = contador1 = contador2 = preco_abaixo = mais_baixo = 0
nome_abaixo = None

while True:
    nome_Produto = str(input("Nome do produto: ")).strip().upper()
    preco_Produto = float(input("Preço do produto: "))
    gasto_tot += preco_Produto
    contador1 += 1

    if contador1 == 1:
        mais_baixo = preco_Produto
        nome_abaixo = nome_Produto

    if preco_Produto < mais_baixo:
        mais_baixo = preco_Produto
        nome_abaixo = nome_Produto

    if preco_Produto > 1000.00:
        contador2 += 1

    while True:
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar in ["S", "N"]:
            break
        else:
            print("Digite apenas 'S' ou 'N'.")
            print("-" * 40)

    if continuar.upper() == "N":
        if contador1 >= 2:
            print(f"Voce gastou um total de R${gasto_tot:.2f}.")
            print(f"Voce comprou {contador2} produtos que custam mais de mil reais.")
            print(f"{nome_abaixo} que custou R${mais_baixo:.2f} foi o produto mais barato comprado.")
        else:
            print(f"Voce gastou um total de R${gasto_tot:.2f}.")
            print(f"Voce comprou {contador1} produto que custa mais de mil Reais.")
            print(f"{nome_abaixo} que custou R${mais_baixo:.2f} foi o produto mais barato comprado.")

        print("Que tenha um bom dia.")
        break


#=================================
#       ALTERNATIVA
#=================================
print("========================================================================================\n")
# Variáveis iniciais
total_gasto = 0
total_produtos = 0
produtos_maior_1000 = 0
produto_mais_barato = ""
preco_mais_barato = None

print("=" * 40)
print("ALTERNATIVA  -->  LOJA SUPER BARATÃO".center(40))
print("=" * 40)

while True:
    nome_produto = input("Nome do produto: ").strip().title()

    while True:
        try:
            preco = float(input("Preço do produto: R$"))
            break
        except ValueError:
            print("Digite um preço válido (apenas números).")

    total_gasto += preco
    total_produtos += 1

    if preco > 1000:
        produtos_maior_1000 += 1

    if preco_mais_barato is None or preco < preco_mais_barato:
        preco_mais_barato = preco
        produto_mais_barato = nome_produto

    # Perguntar se deseja continuar
    while True:
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar in ["S", "N"]:
            break
        else:
            print("Digite apenas 'S' ou 'N'.")

    print("-" * 40)

    if continuar == "N":
        break

# Exibição final
print("\n=== RESUMO DA COMPRA ===")
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Produtos acima de R$1000: {produtos_maior_1000}")
print(f"Produto mais barato: {produto_mais_barato} por R${preco_mais_barato:.2f}")
print("Volte sempre!")







