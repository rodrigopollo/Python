# Leia o nome de 1 pessoa
# Mostre o nome td em maiuscula
# Tambem td em minuscula
# Quantas letras tem (espaço nao conta)
# Quantas letras tem o Primeiro nome


nome = input("Digite um nome: ").strip()

nome_Maiscula = nome.upper()
nome_Minuscula = nome.lower()
qnt_Letras = len(nome) - nome.count(" ")
letras_Primeiro_Nome = nome.find(" ")


print(f"Nome todo em maiusculo: {nome_Maiscula}")
print(f"Nome todo em minusculo: {nome_Minuscula}")
print(f"Quantidade de letras: {qnt_Letras}")
print(f"Quantidade de letras do primeiro nome: {letras_Primeiro_Nome}")

# Alternativa

separa = nome.split()
print("\n", separa)
print(f"Alternativa para saber qntidade de letras primeiro nome: {len(separa[0])}")


