# Mostrar todos numeros pares entre 1 e 50

contador = 0

for i in range(1, 51):
    if i % 2 == 0:
        contador += 1

print(f"Do 1 ao 50 existem um total de {contador} numeros pares.")

# Alternativa

# VARIAVEL
index = 0

# INFO do que o programa ira fazer
print("=" * 60)
print(f"{" ALTERNATIVA 1 E 50 ":^50}")
print("=" * 60)

# Condiçoes
for i in range(2, 51, 2):
    if i % 2 == 0:
        index += 1
        print(i, end=", ")

# Decisao
print(f"\nDo 1 ao 50 existem um total de {contador} numeros pares.")




# Note a primeira resposta esta pensando de uma maneira difernte e nao faz oq o exericio pede
# ele nao mostra os NUMEROS PARES entre 1 e 50, ele mostra QUANTOS NUMEROS PARES tem entre 1 e 50
# mas no 2 aproveitamos o exericio 1 e completamentamos a resposta para ficar ainda mais completa