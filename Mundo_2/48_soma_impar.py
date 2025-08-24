# Some todos os numeros impares que sao multiplos de 3 do 1 ao 500

# Variavel de start
contador = 0

# Condiçao
for i in range(1, 501):
    if i % 3 == 0:
        contador += i

# Decisao
print(f"A soma dos numeros multiplos de 3 entre 1 e 500 eh de {contador}")