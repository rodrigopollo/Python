# Entrada de dados
primeiro_numero = int(input("1º numero: "))
razao = int(input("Razao: "))
decimo = primeiro_numero + (10 - 1) * razao
# Condiçao
for i in range(primeiro_numero, decimo + razao, razao):
    print(f"{i}", end=" -> ")

# Decisao
print("END")