# TUPLA com numero de 0 a 20 por extenso.
# Leia um numero e escreva qual numero voce digitou.
# Se o numero nao estiver entre 0 e 20 nao aceitar e continuar perguntando.

numero = ("zero", "um", "dois", "tres", "quatro", "cinco", "seix", "sete", "oito",
          "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezeseis",
          "dezessete", "dezoito", "dezenove", "vinte")

while True:
    try:
        escolha = int(input("Digite um numero entre 0 e 20: "))
        break
    except ValueError:
        print("ATENÇAO: Digite um numero valido (apenas entre 0 e 20): ")
        print("=" * 35)


print("=" * 35)
print(f"O numero digitado foi: {numero[escolha]}.")
