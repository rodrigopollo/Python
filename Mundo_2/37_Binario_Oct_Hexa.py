# Digite um numero inteiro
# Converta para binario, octal ou hexadecimal, o usuario que esoclhe qual conversao deve ser feita.

# Entrada de dados e info
numero = int(input("Digite um numero: "))
print("""Suas opçoes:
[0] - Binario.
[1] - Papel.
[2] - Tesoura.
""")
opcao = int(input("Qual a opçao: "))

# Calculo
binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:]

# Condiçoes e Decisao
print("-" * 20)
if opcao < 0 or opcao > 2:
    print("ERROR: OPÇAO INVALIDA!")
    exit()
elif opcao == 0:
    print(f"O numero binario de {numero} eh --> {binario}")
elif opcao == 1:
    print(f"O numero octodecimal de {numero} eh --> {octal}")
elif opcao == 2:
    print(f"O numero hexadecimal de {numero} eh --> {hexadecimal}")
    print("-" * 20)





