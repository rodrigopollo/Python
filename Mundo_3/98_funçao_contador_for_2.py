# Funçao com 3 parametros, inicio, fim e passo.
# O programa tem que realizar 3 contagems no total
# 1) De 1 a 10
# 2) De 10 a 0, de -2 em -2
# 3) Uma contagem personalizada.
# NOTE: Programa tem que funcionar com passo positivo e negativo em uma contagem regressiva.
# NOTE: Se o usuario digitar ZERO no passo, o programa vai assumir 1 ou -1 dependendo do objetivo da conta.

# Funçao 1: Condiçoes para PASSO
def condicoes_parametros(inicio, fim, passo):
    # Corrige passo automático caso o usuario digite 0
    if passo == 0:
        passo = 1 if inicio < fim else -1

    # Transforma o passo dependendo da condiçao do contador
    if inicio > fim and passo > 0:
        passo = -passo
    elif inicio < fim and passo < 0:
        passo = -passo

    # Ajusta o fim
    if inicio > fim:
        fim = fim - 1
    else:
        fim = fim + 1

    return inicio, fim, passo


# Funçao 2: Recebe o resultado apos VERIFICADO por CONDIÇOES_PARAMETROS e mostra ao usuario.
def contador(inicio, fim, passo):
    inicio, fim, passo = condicoes_parametros(inicio, fim, passo)

    for i in range(inicio, fim, passo):
        print(i, end=" ")
    print()


# Contadores automaticos.
print("-=" * 22)
print("Contagem de 1 a 10.")
contador(1, 11, 1)
print("-=" * 22)

print("Contagem de 10 ate 0, contando de -2 em -2.")
contador(10, -1, -2)
print("-=" * 22)

# FOR do contador q o usuario decide as regras do inicio, fim e passo.
print("Faça sua contagem personalizada. ")
print("Inicio -> Numero aonde deseja iniciar a contagem.")
inicio_input = int(input("Inicio: "))
print("-=" * 22)
print("FIM -> Numero aonde deseja finalizar a contagem.")
fim_input = int(input("Fim: "))
print("-=" * 22)
print("Passo -> Condiçao da contagem. Exemplos (de 1 em 1), (de 5 em 5) ou (de -1 em -1), etc...")
passo_input = int(input("Passo: "))

contador(inicio_input, fim_input, passo_input)