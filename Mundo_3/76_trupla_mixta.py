# Cria uma TRUPLA com nomes de produtos e seus respectivos preços na sequencia.
# Mostre uma listagem depreços organizando os dados em forma tabular.

produtos = ("Caneta", 2.00, "Leite", 0.96, "Cafe", 5.99, "Mouse", 65.59)

print("-" * 30)
print(f"LISTA DE PREÇOS".center(30))
print("-" * 30)
print(f"{produtos[0]}...............R$ {produtos[1]:.2f}")
print(f"{produtos[2]}................R$ {produtos[3]:.2f}")
print(f"{produtos[4]}.................R$ {produtos[7]:.2f}")
print(f"{produtos[6]}................R$ {produtos[7]:.2f}")
print("/" * 30)

#=======================
#     ALTERNATIVA
#=======================
print(f"ALTERNATIVA".center(30))
print("/" * 30)


for i in range(0, len(produtos)):
    if i % 2 == 0:
        # Mostra o nomes do produta alinha a esquerda (:.<30) seguido de 30..... Sem saltar linha no final.
        print(f"{produtos[i]:.<30}", end=" ")
    else:
        # Mostra o preço do produto. (:>7) alinha a direita com 7 espaços com 2 casas decimais (.2f)
        print(f"R${produtos[i]:>7.2f}")



















