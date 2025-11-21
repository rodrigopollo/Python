# Programa para testar uma lista e verificar se esta contando corretamente
# os valores desejados, no caso a quantidade de 5 inseridas.
# Mostra passo a passo como esta indo a contagem para ter certeza q esta funcionando.


numeros = []

while True:
    valor = int(input("Digite um número: "))
    numeros.append(valor)

    cinco = numeros.count(5)
    print(f"Números atuais: {numeros}")
    print(f"Quantidade de 5: {cinco}")

    sair = input("Deseja sair? [S/N]: ").strip().upper()
    if sair == "S":
        break

print("-=" * 20)
print(f"Numeros digitados: {numeros}")
print(f"Total de numero 5 digitados: {cinco}")
print("-=" * 20)
