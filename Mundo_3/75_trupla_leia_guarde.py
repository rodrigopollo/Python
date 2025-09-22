# Leia 4 valores e armazene em uma TRUPLA
# Mostre qntas vezes aparece 9
# Qual o index do primeiro numero 3
# Quais fora os numeros PARES

# Trupla vazia
numeros = pares = ()
tres = 0

# Por cada loop add 1 valor dentro da TRUPLA.
for i in range(4):
    valor = int(input("Digite um valor: "))
    numeros += (valor,)

    if valor == 3:
        tres += 1
    if valor % 2 == 0:
        pares += (valor,)

# Conta quantas vezes aparece o numero 9
qnt_nove = numeros.count(9)

print("-=" * 30)
print(f"Voce digitou {numeros}")
print(f"O  9 apareceu {qnt_nove} vezes.")

# Verificaçao se foi ou n digitado o numero 3
if tres >= 1:
    print(f"O 3 foi inserido pela 1º vez no index {numeros.index(3) + 1}")
else:
    print(f"O numero 3 nao foi digitado.")

# Verificação se foi ou nao digitados numeros pares
if pares:
    print(f"Os numeros {pares} sao pares.")
else:
    print("Nao foram inseridos numeros pares")



#=================================
#          ALTERNATIVA
#=================================
print("/" * 80)


# Tupla vazia
numeros = ()
pares = ()

print("=" * 40)
print("Digite 4 valores inteiros")
print("=" * 40)

for i in range(4):
    valor = int(input(f"Valor {i + 1}: "))
    numeros += (valor,)  # Adiciona o valor na tupla

    if valor % 2 == 0:
        pares += (valor,)

# Contagem do número 9
qtd_nove = numeros.count(9)

print("=" * 40)
print(f"Você digitou os valores: {numeros}")
print(f"O número 9 apareceu {qtd_nove} vez(es).")

# Posição do número 3
if 3 in numeros:
    posicao = numeros.index(3) + 1  # posição começa no 1
    print(f"O número 3 apareceu pela primeira vez na posição {posicao}.")
else:
    print("O número 3 não foi digitado.")

# Mostra os números pares
if pares:
    print(f"Os números pares digitados foram: {pares}")
else:
    print("Nenhum número par foi digitado.")
print("=" * 40)



