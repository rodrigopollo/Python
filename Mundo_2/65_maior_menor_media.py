# Leia numero INT e pergunte se quer continuar
# Mostrar MEDIA de todos os valores inseridos
# Mostrar o MAIOR de todos os valores inseridos
# Mostrar o MENOR de todos os valores inseridos

contador = soma = media = None
sair = maior = menor = None

while sair != "S":
    numero = int(input("Digite um numero: "))
    contador += 1
    soma += numero
    media = soma / contador

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    sair = str(input("Deseja continuar [S/N]: ")).strip().upper()

print(f"Soma = {soma}")
print(f"Meida = {media:.1f}")
print(f"O maior numero foi  = {maior}")
print(f"O menor numero foi  = {menor}")


# Logica de achar o maior e menor:
# Primeiro vc tem que dar 1 valor as VAR (maior, menor) pra isso assim que o programa começar o
# contador vai passar de (zero) -> 1, entao voce coloca 1 condição quando o programa começar
# q eh qndo o contador passa a ser 1.
# Eu quero que maior e menor sejam iguais ao primeiro numero que voce digitar.
# Depois voce começa a fazer verificaçoes, IF o proximo numero digitado for > que MAIOR
# ai voce quer substituir o valor atual da VARIAVEL pelo maior NUMERO digitado.
# SENAO se o valor for menos faça a mesma coisa.