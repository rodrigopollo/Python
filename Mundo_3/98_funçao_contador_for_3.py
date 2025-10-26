def condicoes_parametros(inicio, fim, passo):
    if passo == 0:
        passo = 1 if inicio < fim else -1
    if inicio > fim and passo > 0:
        passo = -passo
    elif inicio < fim and passo < 0:
        passo = -passo
    if inicio > fim:
        fim = fim - 1
    else:
        fim = fim + 1
    return inicio, fim, passo


def contador(inicio, fim, passo):
    inicio, fim, passo = condicoes_parametros(inicio, fim, passo)

    for i in range(inicio, fim, passo):
        print(i, end=" ")
    print()


contador(1, 11, 1)
contador(10, -1, -2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))
