
def contador(inicio, fim, passo):
    # 10, 0, -1
    # passo vai de 0 pra 1
    if passo == 0:
        passo = 1
    # passo sempre positivo
    if passo < 0:
        passo = abs(passo)
    # passo se torna negativo so nesse cenario
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')

    print()

contador(1,10,0)
contador(10,0,2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))