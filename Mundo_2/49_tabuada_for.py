# tabuado com FOR

# Informaçao descritiva
print(f"{" Tabuada ":=^40}")

# Entrada de dados
numero = int(input("\nDigite o numero que deseja saber a tabuada: "))

# Condiçao e Decisao
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")