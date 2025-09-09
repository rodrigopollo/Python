# Leia numeros inteiros ate inserir 999 q sera a condiçao de saida.
# Mostre a soma de todos os numeros inseridos qndo voce sair.
# Desconsiderar o Flag (999)

soma = numero = None

while numero != 999:
    numero = int(input("Digite um numero: "))
    if numero != 999:
        print(f"{numero}")
        soma += numero
print(f"A soma de todos os numeros eh = {soma}")

#=======================
#     ALTERNATIVA
#=======================

n1 = soma1 = None
num = int(input("Digite um numero: "))

while num != 999:
    soma += num
    num = int(input("Digite um numero: "))

print(f"A soma de todos os numeros eh = {soma1}")



# Na alternativa usamos
#           num = int(input("Digite um numero: "))
# para estabelecer um limete, ou seja, ja seja na linha 19 ou na linha 23, sempre q eu digitar 1 numero
# ele vai passar pela vericaçao do while na linha 21, entao sempre q for 999 o while vai detectar
# e vai sair do programa.



