
# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input("Insira um numero inteiro: "))

antes = numero - 1
depois = numero + 1

print(f"O numero que voce colocou foi o {numero}")
print(f"\nO numero antecessor de {numero} eh {antes}")
print(f"O numero sucessor de {numero} eh {depois}")

#           -----  ALTERNATIVA ----

print(f"\nO numero antecessor eh {numero - 1}")
print(f"O numero sucessor eh {numero + 1}")