# Leia um nome
# Mostre somente o Primeiro e o Ultimo nome

nome = input("Digite um nome: ").strip()

separar_Nome = nome.split()
primeiro_Nome = separar_Nome[0]
ultimo_Nome = separar_Nome[-1]

print(f"Primeiro nome digitado: {primeiro_Nome}")
print(f"Segundo nome digitado: {ultimo_Nome}")


# NOTE.: como a variavel NOME ja esta splitada o -1 serve para dizer ao python que oq voce
# quer eh a ultima palavra que for escrita na variavel NOME