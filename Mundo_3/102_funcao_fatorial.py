# Usando funçao.
# Fazer o FATORIAL
# Perguntar ao usuario se ele quer ver o calculo ou so o resultado.
from math import factorial


def calculo_fatorial(numero):
    return factorial(numero)


print(f"{'   CALCULO FATORIAL'}")
print('-' * 30)
numero_input = int(input("Digite um numero: "))
resultado = calculo_fatorial(numero_input)

# LOOP: So aceita S ou N para escolher entre ver o calculo completo ou so o resultado do FATORIAL
while True:
    mostrar_calculo = input("Deseja ver o calculo do fatorial? [S/N]: ").strip().upper()[0]

    if mostrar_calculo in "S":
        for i in range(numero_input, 0, -1):
            print(f"{i}", end="")
            if i > 1:
                print(f" x ",end=' ')
        print(f" = {resultado}")
        break

    elif mostrar_calculo in "N":
        print(f"Fatorial de {numero_input}: {resultado}")
        break
    else:
        print("Digite apenas S ou N.")
